from rdflib import Graph
import networkx as nx
from pyvis.network import Network

# Charger le graphe RDF
rdf_data = """
@prefix db: <http://dbpedia.org/resource/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix mads: <http://www.loc.gov/mads/rdf/v1#> .
@prefix cwrc: <https://sparql.cwrc.ca/ontologies/cwrc#> .
@prefix mo: <http://purl.org/ontology/mo/> . 
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

db:Mozart
    rdf:label "Wolfgang Amadeus Mozart" ;
    rdf:type db:Person, mo:Composer ;
    mads:birthPlace "Salzbourg" ;
    mads:birthDate "1756-01-27"^^xsd:date ;
    mads:deathPlace "Vienne" ;
    mads:deathDate "1791-12-05"^^xsd:date ;
    cwrc:sonOf db:Leopold_Mozart ;
    owl:spouse db:Constance_Weber .

db:Leopold_Mozart
    rdf:label "Léopold Mozart" ;
    rdf:type db:Person .

db:Constance_Weber
    rdf:label "Constance Weber" ;
    rdf:type db:Person .

db:LaFluteEnchantee 
    rdf:type db:Oeuvre ;
    rdf:type db:Opera ;
    rdf:label "La flute enchantée".

db:Jupiter 
    rdf:type db:Oeuvre ;
    rdf:type db:Symphonie ;
    mo:movement db:MouvementsJupiter.

db:MouvementsJupiter 
    rdf:type rdf:Seq ;
    rdf:_1 "Allegro Vivace" ;
    rdf:_2 "Andante Cantabile" ;
    rdf:_3 "Menuetto" ;
    rdf:_4 "Molto Allegro" .

db:OchestreSymphoniqueDeLondres
    rdf:label "L'orcestre symphonique de Londres" ;
    rdf:type mo:Orchestration, mo:MusicGroup.

db:JupiterRecording 
    rdf:type mo:Recording ;
    mo:recording_of db:Jupiter ;
    mo:performer db:OchestreSymphoniqueDeLondres ;
    mo:conductor db:Claudio_Abbado ;
    mo:recorded_in "1980"^^xsd:gYear .

db:Claudio_Abbado 
    rdf:type db:Person ;
    rdf:label "Claudio Abbado" .
"""

# Charger le graphe RDF avec rdflib
g = Graph()
g.parse(data=rdf_data, format="turtle")

# Créer un graphe NetworkX
nx_graph = nx.DiGraph()

# Ajouter les triplets RDF au graphe NetworkX
for subj, pred, obj in g:
    subj, pred, obj = str(subj), str(pred), str(obj)
    nx_graph.add_edge(subj, obj, label=pred)

# Visualiser avec Pyvis
net = Network(notebook=True, directed=True)
for node in nx_graph.nodes():
    net.add_node(node, label=node.split("/")[-1])  # Utiliser le dernier segment de l'URI comme label

for edge in nx_graph.edges(data=True):
    net.add_edge(edge[0], edge[1], title=edge[2]["label"].split("/")[-1])

# Générer la visualisation
net.show("rdf_graph.html")
