from fastapi import APIRouter
from SPARQLWrapper import JSON

from fastapi_globals import g
from utils import SPARQLExceptions
from fastapi_cache.decorator import cache

router = APIRouter()


@router.get("/cases_and_deaths")
@cache()
async def covid_cases():
    g.sparql.setQuery("""
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        SELECT DISTINCT ?period (SUM(?newCases) AS ?numOfCovidCases) (ROUND((?numOfCovidCases*100 / 30))/100 AS ?casesRatio) (SUM(?newDeaths) AS ?numOfDeaths) (ROUND((?numOfDeaths*100 / 30))/100 AS ?deathsRatio)
        WHERE {
            ?day lao:hasDate ?date ;
                 lao:hasNewCases ?newCases ;
                 lao:hasNewDeaths ?newDeaths .
                 
            # convert to strings
            BIND(STR(YEAR(?date)) AS ?year)
            BIND(STR(MONTH(?date)) AS ?month)
            # pad with zeros
            BIND(CONCAT("00", ?year) AS ?paddedYear)
            BIND(CONCAT("0000", ?month) AS ?paddedMonth)
            # extract the rxight number of digits from the padded strings
            BIND(SUBSTR(?paddedYear, STRLEN(?paddedYear)-3) AS ?fourDigitYear)
            BIND(SUBSTR(?paddedMonth, STRLEN(?paddedMonth)-1) AS ?twoDigitMonth)
            # put it all back together
            BIND(CONCAT(?fourDigitYear, "-", ?twoDigitMonth) AS ?period)
            
            FILTER (xsd:date(?date) >= "2020-01-01"^^xsd:date && xsd:date(?date) <= "2022-12-31"^^xsd:date)
        }
        GROUP BY ?period
        ORDER BY ASC(?period)
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
            "period": result["period"]["value"],
            "numOfCovidCases": int(result["numOfCovidCases"]["value"]),
            "casesRatio": float(result["casesRatio"]["value"]),
            "numOfDeaths": int(result["numOfDeaths"]["value"]),
            "deathsRatio": float(result["deathsRatio"]["value"]),
        }
        for result in results["results"]["bindings"]
    ]



