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



