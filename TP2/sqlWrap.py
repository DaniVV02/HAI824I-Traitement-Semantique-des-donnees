from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

# Définition du point d'entrée SPARQL
sparql_endpoint = "http://localhost:3030/mAbKG/sparql"

# Liste des requêtes à exécuter
queries = {
    "1": """
        SELECT * WHERE { ?mAb <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://www.imgt.org/imgt-ontology#INN> . } LIMIT 20
    """,
    "2": """
        SELECT * WHERE { ?mAb <http://semanticscience.org/resource/SIO_000291> ?obj . } LIMIT 20
    """,
    "3": """
        SELECT * WHERE { ?mAb <https://www.imgt.org/imgt-ontology#hasClinicalIndication> ?obj . } LIMIT 10
    """,
    "4": """
        SELECT * WHERE { ?mAb <http://www.bioassayontology.org/bao#BAO_0000196> ?obj . } LIMIT 20
    """,
    "5": """
        SELECT * WHERE { ?mAb <https://www.imgt.org/imgt-ontology#hasProduct> ?obj . } LIMIT 30
    """    
}

# Fonction pour exécuter une requête et sauvegarder les résultats
def execute_query_and_save(query, query_id):
    try:
        sparql = SPARQLWrapper(sparql_endpoint)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        # ou autre format : sparql.setReturnFormat(XML)

        results = sparql.query().convert()
        #  ou sparql.queryAndConvert()
        
        # print(results.toxml())

        # print(results.serialize())

        # Extraction des résultats
        data = []
        for result in results["results"]["bindings"]:
            row = {key: result[key]["value"] for key in result}
            data.append(row)

        # Sauvegarde en CSV si on a des résultats
        if data:
            df = pd.DataFrame(data)
            filename = f"requete_{query_id}.csv"
            df.to_csv(filename, index=False)
            print(f"✅ Résultats sauvegardés dans {filename}")
        else:
            print(f"⚠️ Aucune donnée pour la requête {query_id}")

    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de la requête {query_id} : {e}")

# Exécuter toutes les requêtes et sauvegarder les résultats
for query_id, query in queries.items():
    execute_query_and_save(query, query_id)
