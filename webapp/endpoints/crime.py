from fastapi import APIRouter
from SPARQLWrapper import JSON, SPARQLExceptions

from fastapi_globals import g


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

    data = []
    for result in results["results"]["bindings"]:
        data.append(result["data"]["value"])

    return data


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
