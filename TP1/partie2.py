from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD, OWL

# Création du graphe RDF
g = Graph()

# Définition des namespaces
RDF= Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
DB = Namespace("http://dbpedia.org/resource/")
MADS = Namespace("http://www.loc.gov/mads/rdf/v1#")
CWRC = Namespace("https://sparql.cwrc.ca/ontologies/cwrc#")
MO = Namespace("http://purl.org/ontology/mo/")
EX = Namespace("http://example.org/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")


# Ajout des préfixes au graphe
g.bind("db", DB)
g.bind("mads", MADS)
g.bind("cwrc", CWRC)
g.bind("mo", MO)
g.bind("owl", OWL)
g.bind("xsd", XSD)

# Ajout des entités et relations
g.add((DB.Mozart, RDF.type, DB.Person))
g.add((DB.Mozart, RDF.type, MO.Composer))
g.add((DB.Mozart, MADS.birthPlace, Literal("Salzbourg")))
g.add((DB.Mozart, MADS.birthDate, Literal("1756-01-27", datatype=XSD.date)))
g.add((DB.Mozart, MADS.deathPlace, Literal("Vienne")))
g.add((DB.Mozart, MADS.deathDate, Literal("1791-12-05", datatype=XSD.date)))
g.add((DB.Mozart, CWRC.sonOf, DB.Leopold_Mozart))
g.add((DB.Mozart, OWL.spouse, DB.Constance_Weber))

# Ajout de Léopold Mozart et Constance Weber
g.add((DB.Leopold_Mozart, RDF.type, DB.Person))
g.add((DB.Leopold_Mozart, RDF.label, Literal("Léopold Mozart")))

g.add((DB.Constance_Weber, RDF.type, DB.Person))
g.add((DB.Constance_Weber, RDF.label, Literal("Constance Weber")))

# Ajout de La Flûte Enchantée
g.add((DB.LaFluteEnchantee, RDF.type, DB.Oeuvre))
g.add((DB.LaFluteEnchantee, RDF.type, DB.Opera))
g.add((DB.LaFluteEnchantee, RDF.label, Literal("La Flûte Enchantée")))

# Ajout de la Symphonie Jupiter et ses mouvements
g.add((DB.Jupiter, RDF.type, DB.Oeuvre))
g.add((DB.Jupiter, RDF.type, DB.Symphonie))
g.add((DB.Jupiter, MO.movement, DB.MouvementsJupiter))

g.add((DB.MouvementsJupiter, RDF.type, RDF.Seq))
g.add((DB.MouvementsJupiter, URIRef(RDF["_1"]), Literal("Allegro Vivace")))
g.add((DB.MouvementsJupiter, URIRef(RDF["_2"]), Literal("Andante Cantabile")))
g.add((DB.MouvementsJupiter, URIRef(RDF["_3"]), Literal("Menuetto")))
g.add((DB.MouvementsJupiter, URIRef(RDF["_4"]), Literal("Molto Allegro")))

# Ajout de l'Orchestre Symphonique de Londres
g.add((DB.OchestreSymphoniqueDeLondres, RDF.label, Literal("L'orchestre symphonique de Londres")))
g.add((DB.OchestreSymphoniqueDeLondres, RDF.type, MO.Orchestration))
g.add((DB.OchestreSymphoniqueDeLondres, RDF.type, MO.MusicGroup))

# Ajout de l'enregistrement de Jupiter
g.add((DB.JupiterRecording, RDF.type, MO.Recording))
g.add((DB.JupiterRecording, MO.recording_of, DB.Jupiter))
g.add((DB.JupiterRecording, MO.performer, DB.OchestreSymphoniqueDeLondres))
g.add((DB.JupiterRecording, MO.conductor, DB.Claudio_Abbado))
g.add((DB.JupiterRecording, MO.recorded_in, Literal("1980", datatype=XSD.gYear)))

# Ajout de Claudio Abbado
g.add((DB.Claudio_Abbado, RDF.type, DB.Person))
g.add((DB.Claudio_Abbado, RDF.label, Literal("Claudio Abbado")))

# Sauvegarde du graphe RDF en Turtle
with open("mozart_graph.ttl", "w", encoding="utf-8") as f:
    f.write(g.serialize(format="turtle"))

# Affichage du graphe RDF (en Turtle)
print(g.serialize(format="turtle"))
