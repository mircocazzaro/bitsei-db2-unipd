from fastapi import APIRouter
from SPARQLWrapper import JSON

from fastapi_globals import g
from utils import SPARQLExceptions

router = APIRouter()


@router.get("")
async def crime_codes():
    g.sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
    
        SELECT DISTINCT ?crimeCode WHERE {
            ?crime lao:crimeCode ?crimeCode
        }
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    return {"data": results["results"]["bindings"]}


@router.get("/codes")
async def crime_codes():
    g.sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema/>
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        SELECT DISTINCT ?data WHERE {
            ?crime 	lao:crimeCode 	?crimeCode;
                    lao:crimeDesc 	?crimeDesc.
            FILTER(datatype(?crimeCode) = xsd:integer)
            BIND(CONCAT(?crimeDesc, "@", STR(?crimeCode)) AS ?data)
        }
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(results["results"]["bindings"]) == 0:
        return []

    return [result["data"]["value"] for result in results["results"]["bindings"]]


@router.get("/weapon")
async def crime_weapon(
        crime_code: str
):
    g.sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema/>
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        
        SELECT ?crimeDesc ?weaponDesc (COUNT(?weapon) AS ?we_count) WHERE {
          ?crimeEvent lao:isOfType ?crime;
                      lao:usedWeapon ?weapon.
          ?crime lao:crimeCode "%s"^^xsd:int;
                 lao:crimeDesc ?crimeDesc.
          ?weapon lao:weaponDesc ?weaponDesc.
        }
        GROUP BY ?weaponDesc ?crimeDesc
        ORDER BY DESC(?we_count)
    """ % crime_code)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(results["results"]["bindings"]) == 0:
        return {"data": []}

    data = {'name': results["results"]["bindings"][0]["crimeDesc"]["value"], 'children': []}
    for result in results["results"]["bindings"]:
        data['children'].append({
            'name': f'{result["weaponDesc"]["value"]} - {int(result["we_count"]["value"])}',
        })

    return data


@router.get("/category-month")
async def category_month():
    g.sparql.setQuery("""
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        SELECT DISTINCT ?month ?crimeCat (COUNT(?crimeEvent) AS ?crimeCount) WHERE {
            ?crimeEvent a                   lao:CrimeEvent ;
                        lao:isOfType        ?crime ;
                        lao:occurredOnDate  ?day.

            ?crime a ?crimeCat.
            
            FILTER(?crimeCat in (lao:ViolentCrime, lao:PropertyCrime, lao:PublicOrderCrime, lao:WhiteCollarCrime, lao:SexualCrime)).

            ?day a          lao:Day ;
                lao:hasDate ?date .
            
            BIND(xsd:int(MONTH(?date)) AS ?month) .
            
            FILTER(YEAR(?date) = 2020)
        }
        GROUP BY ?crimeCat ?month
        ORDER BY ?month
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(results["results"]["bindings"]) == 0:
        return {"data": []}

    transformed_data = {}

    # Iterate through the original array
    for result in results["results"]["bindings"]:
        # month = int(result["month"]["value"]),
        crime_cat = result["crimeCat"]["value"].split('/')[-1]
        crime_count = int(result["crimeCount"]["value"])

        # If the dataset entry doesn't exist, create an entry with an empty list
        if crime_cat not in transformed_data:
            transformed_data[crime_cat] = {
                "label": crime_cat,
                "data": [],  # Initialize with empty for each month
                # "borderColor": "#000000",
                # "backgroundColor": "#000000"
            }

        # Add the crime_count to the corresponding month in the data list
        transformed_data[crime_cat]["data"].append(crime_count)

    return list(transformed_data.values())


@router.get("/category-event-by-area")
async def category_event_by_area():
    g.sparql.setQuery("""
        PREFIX lao: <http://www.bitsei.it/losAngelesOntology/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        SELECT DISTINCT ?areaName ?areaAcronym (COUNT(?crimeEvent) AS ?crimeEvents) (((ROUND(?crimeEvents * 100 / 30)) / 100) AS ?ratio) 
        WHERE {
            ?crimeEvent lao:occurredOnDate ?day ;
                        lao:occurredInLocation ?location .
            ?day lao:hasDate ?date .
            ?location lao:belongsToArea ?area .
            ?area lao:areaName ?areaName ;
                  lao:areaAcronym ?areaAcronym .
        }
        GROUP BY ?areaName ?areaAcronym
        ORDER BY DESC(?crimeEvents)
    """)

    g.sparql.setReturnFormat(JSON)

    try:
        results = g.sparql.query().convert()
    except SPARQLExceptions as e:
        return {"data": e.args}

    if len(results["results"]["bindings"]) == 0:
        return {"data": []}

    data = []
    # Iterate through the original array
    for result in results["results"]["bindings"]:
        data.append({
            "acronym": result["areaAcronym"]["value"],
            "ratio": float(result["ratio"]["value"]),
        })

    return data
