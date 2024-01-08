from fastapi import APIRouter
from SPARQLWrapper import JSON
from fastapi_cache.decorator import cache

from fastapi_globals import g
from utils import SPARQLExceptions

router = APIRouter()


@router.get("/")
@cache()
async def open_closed_businesses():
    g.sparql.setQuery("""
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        SELECT ?cityName (COUNT(?business) AS ?numBusinesses20) ?numBusinesses21 ?numBusinesses22 WHERE {
            ?business lao:locatedInCity ?city ;
                      lao:openedOnDate ?day .
            ?day lao:hasDate ?date .
            ?city lao:cityName ?cityName .   
        
            {
                SELECT ?cityName (COUNT(?business) AS ?numBusinesses21) ?numBusinesses22 WHERE {
                    ?business lao:locatedInCity ?city ;
                              lao:openedOnDate ?day .
                    ?day lao:hasDate ?date .
                    ?city lao:cityName ?cityName .   
                    {
                        SELECT ?cityName (COUNT(?business) AS ?numBusinesses22) WHERE {
                            ?business lao:locatedInCity ?city ;
                                      lao:openedOnDate ?day .
                            ?day lao:hasDate ?date .
                            ?city lao:cityName ?cityName .   
        
                            FILTER (xsd:date(?date) >= "2022-01-01"^^xsd:date && xsd:date(?date) <= "2022-12-31"^^xsd:date)
                        }
                        GROUP BY (?cityName)
                        ORDER BY DESC(?numBusinesses22)
                    }
                    FILTER (xsd:date(?date) >= "2021-01-01"^^xsd:date && xsd:date(?date) <= "2021-12-31"^^xsd:date)
                }
                GROUP BY ?cityName ?numBusinesses22
                ORDER BY DESC(?numBusinesses21)
            }
            
            FILTER (xsd:date(?date) >= "2020-01-01"^^xsd:date && xsd:date(?date) <= "2020-12-31"^^xsd:date)
        }
        GROUP BY ?cityName ?numBusinesses21 ?numBusinesses22
        ORDER BY DESC(?numBusinesses20)
        LIMIT 50
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(results["results"]["bindings"]) == 0:
        return {"data": []}

    return [
        {
            "cityName": result["cityName"]["value"],
            "numBusinesses20": result["numBusinesses20"]["value"],
            "numBusinesses21": result["numBusinesses21"]["value"],
            "numBusinesses22": result["numBusinesses22"]["value"],
        }
        for result in results["results"]["bindings"]
    ]


@router.get("/count")
@cache()
async def count_closed_businesses():
    g.sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema/>
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        SELECT ?area_name (COUNT(?crimeEvent) as ?countCrimeEvent) WHERE {
            ?crimeEvent lao:occurredInLocation 	?location.
            ?location 	lao:belongsToArea 		?area.
            ?area		lao:areaName			?area_name.
        }
        GROUP BY ?area_name
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(results["results"]["bindings"]) == 0:
        return {"data": []}

    return [
        {
            "area_name": result["area_name"]["value"],
            "count": int(result["countCrimeEvent"]["value"]),
        }
        for result in results["results"]["bindings"]
    ]


@router.get("/open-closed-by-naics")
@cache()
async def open_closed_business_by_naics():
    g.sparql.setQuery("""
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        SELECT DISTINCT ?naicsDesc (COUNT(?openBusiness) AS ?openedBusinesses) (ROUND(?openedBusinesses*1000 / ?totBusinesses)/1000 AS ?ratio) 
        WHERE {
            ?openBusiness lao:openedOnDate ?day ;
                          lao:hasNaics ?naics .
            ?day lao:hasDate ?date .
            ?naics lao:naicsCode ?naicsCode ;
                   lao:naicsDescription ?naicsDesc .
            # convert to strings
            BIND(STR(YEAR(?date)) AS ?year)
            BIND(STR(MONTH(?date)) AS ?month)
            # pad with zeros
            BIND(CONCAT("00", ?year) AS ?paddedYear)
            BIND(CONCAT("0000", ?month) AS ?paddedMonth)
            # extract the right number of digits from the padded strings
            BIND(SUBSTR(?paddedYear, STRLEN(?paddedYear)-3) AS ?fourDigitYear)
            BIND(SUBSTR(?paddedMonth, STRLEN(?paddedMonth)-1) AS ?twoDigitMonth)
            # put it all back together
            BIND(CONCAT(?fourDigitYear, "-", ?twoDigitMonth) AS ?period)
            
            FILTER (xsd:date(?date) >= "2020-01-01"^^xsd:date && xsd:date(?date) <= "2022-12-31"^^xsd:date)
        
            {
                SELECT DISTINCT (COUNT(?openBus) AS ?totBusinesses) 
                WHERE {
                    ?openBus lao:openedOnDate ?openDay .
                    ?openDay lao:hasDate ?openDate .
                    FILTER (xsd:date(?openDate) >= "2020-01-01"^^xsd:date && xsd:date(?openDate) <= "2022-12-31"^^xsd:date)
                }                        
            }
        }
        GROUP BY ?naicsCode ?naicsDesc ?totBusinesses
        ORDER BY DESC(?openedBusinesses)
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        opened_results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(opened_results["results"]["bindings"]) == 0:
        return {"data": []}

    g.sparql.setQuery("""
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        
        SELECT DISTINCT ?naicsDesc (COUNT(?closeBusiness) AS ?closedBusinesses) (ROUND(?closedBusinesses*1000 / ?totBusinesses)/1000 AS ?ratio) 
        WHERE {
            ?closeBusiness lao:closedOnDate ?day ;
                          lao:hasNaics ?naics .
            ?day lao:hasDate ?date .
            ?naics lao:naicsCode ?naicsCode ;
                   lao:naicsDescription ?naicsDesc .
            # convert to strings
            BIND(STR(YEAR(?date)) AS ?year)
            BIND(STR(MONTH(?date)) AS ?month)
            # pad with zeros
            BIND(CONCAT("00", ?year) AS ?paddedYear)
            BIND(CONCAT("0000", ?month) AS ?paddedMonth)
            # extract the right number of digits from the padded strings
            BIND(SUBSTR(?paddedYear, STRLEN(?paddedYear)-3) AS ?fourDigitYear)
            BIND(SUBSTR(?paddedMonth, STRLEN(?paddedMonth)-1) AS ?twoDigitMonth)
            # put it all back together
            BIND(CONCAT(?fourDigitYear, "-", ?twoDigitMonth) AS ?period)
            
            FILTER (xsd:date(?date) >= "2020-01-01"^^xsd:date && xsd:date(?date) <= "2022-12-31"^^xsd:date)
        
            {
                SELECT DISTINCT (COUNT(?closeBus) AS ?totBusinesses) 
                WHERE {
                    ?closeBus lao:closedOnDate ?closeDay .
                    ?closeDay lao:hasDate ?closeDate .		
                    FILTER (xsd:date(?closeDate) >= "2020-01-01"^^xsd:date && xsd:date(?closeDate) <= "2022-12-31"^^xsd:date)
                }                        
            }
        }
        GROUP BY ?naicsCode ?naicsDesc ?totBusinesses
        ORDER BY DESC(?closedBusinesses)
        """
                      )

    g.sparql.setReturnFormat(JSON)

    try:
        closed_results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(closed_results["results"]["bindings"]) == 0:
        return {"data": []}

    # combine the two results and merge them by their naicsDesc
    results = []
    for opened_result in opened_results["results"]["bindings"]:
        results.extend(
            {
                "naicsDesc": opened_result["naicsDesc"]["value"],
                "openedBusinesses": opened_result["openedBusinesses"]["value"],
                "closedBusinesses": closed_result["closedBusinesses"]["value"],
            }
            for closed_result in closed_results["results"]["bindings"]
            if opened_result["naicsDesc"]["value"]
            == closed_result["naicsDesc"]["value"]
        )
    return results
