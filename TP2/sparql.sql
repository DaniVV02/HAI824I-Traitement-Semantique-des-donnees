-- Partie 1

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX db: <http://dbpedia.org/resource/> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX mads: <http://www.loc.gov/mads/rdf/v1#> 
PREFIX cwrc: <https://sparql.cwrc.ca/ontologies/cwrc#> 
PREFIX mo: <http://purl.org/ontology/mo/> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 


SELECT ?sub ?pred ?obj WHERE {
  db:Mozart ?pred ?obj .
} LIMIT 50


SELECT ?sub ?pred ?obj WHERE {
  db:Mozart <https://sparql.cwrc.ca/ontologies/cwrc#sonOf> ?obj .
} LIMIT 50


SELECT ?sub ?pred ?obj WHERE {
  db:Mozart cwrc:sonOf ?obj .
} LIMIT 50

SELECT ?sub ?pred ?obj WHERE {
  db:Mozart owl:spouse ?obj .
} LIMIT 50


SELECT ?sub ?pred ?obj WHERE {
  db:Mozart mads:deathPlace ?obj .
} LIMIT 50


-- Partie 2



-- 1.

SELECT *
WHERE {
  ?mAb rdf:type imgt:INN .
}
LIMIT 20

-- ou aussi

SELECT ?mAb ?pred ?obj
WHERE {
  ?mAb rdf:type imgt:INN .
}
LIMIT 20


-- 2.

SELECT *
WHERE {
  ?mAb sio:SIO_000291 ?obj .
}
LIMIT 20

-- 3.

SELECT *
WHERE {
  ?mAb imgt:hasClinicalIndication ?obj .
}
LIMIT 10

-- 4.

SELECT *
WHERE {
  ?mAb bao:BAO_0000196 ?obj .
}
LIMIT 20

-- 5.

SELECT * 
WHERE {
  ?mAb imgt:hasProduct ?product .
  ?product imgt:hasStudyProduct ?study .
} LIMIT 30
 

-- 6. 

SELECT distinct * WHERE {
  ?mAb imgt:inn_name ?inn_name .
} LIMIT 20

-- a.


SELECT *
WHERE {
  ?mAb imgt:inn_name ?obj .
}
LIMIT 30

SELECT *
WHERE {
  ?mAb imgt:inn_name "belimumab" .
  ?mAb2 imgt:inn_name "oxelumab" .
  ?mAb3 imgt:inn_name "relatlimab" .
}

-- ou aussi

SELECT distinct * WHERE {
  ?mAb imgt:inn_name ?inn_name .
  Filter (Contains(?inn_name,"belimumab") || Contains(?inn_name,"oxelumab")|| Contains(?inn_name,"relatlimab"))
} LIMIT 20
-- b.

SELECT *
WHERE {
  ?mAb imgt:inn_name "belimumab" .
  
  ?mAb imgt:hasConstruct ?construction .
  
  ?construction ?cPredicat ?cKnowledge .
  
  ?mAb sio:SIO_000291 ?target
}

--ou plutot ceci :

SELECT distinct *
WHERE {
  ?mAb imgt:inn_name "belimumab" .
  ?mAb imgt:hasConstruct ?const .
  ?const obo:BFO_0000051 ?kowledge .
  ?const imgt:hasImgtLabel ?imgtlabel .
  ?const imgt:hasReceptorFormat ?receptformat .
  ?mAb sio:SIO_000291 ?cible .
} 


SELECT *
WHERE {
  ?mAb imgt:inn_name "oxelumab" .
  
  ?mAb imgt:hasConstruct ?construction .
  
  ?construction ?cPredicat ?cKnowledge .
  
  ?mAb sio:SIO_000291 ?target
}

SELECT *
WHERE {
  ?mAb imgt:inn_name "relatlimab" .
  
  ?mAb imgt:hasConstruct ?construction .
  
  ?construction ?cPredicat ?cKnowledge .
  
  ?mAb sio:SIO_000291 ?target
}

-- c.

SELECT *
WHERE {
  ?mAb imgt:inn_name "oxelumab" .
  
  ?mAb imgt:hasProduct ?product .
  
  ?product imgt:hasStudyProduct ?pKnowledge .
  
  ?pKnowledge imgt:hasClinicalPhase ?clinicalPhase .
  
}

SELECT *
WHERE {
  ?mAb imgt:inn_name "relatlimab" .
  
  ?mAb imgt:hasProduct ?product .
  
  ?product imgt:hasStudyProduct ?pKnowledge .
  
  ?pKnowledge imgt:hasClinicalPhase ?clinicalPhase .
  
}



-- d . Pas fini

SELECT DISTINCT *
WHERE {
  ?mAb imgt:inn_name "relatlimab" ;
  
  imgt:hasClinicalIndication ?ind ;
  sio:SIO_000291 ?target ;
  imgt:hasConstruct ?const ;
  bao:BAO_0000196 ?moa ;
  imgt:hasProduct ?prod .
  ?const ?predcons ?objcons .
  ?target obo:RO_0002162 ?spec .
  // a finir
  
  
  
  filter contains(str(?ind), "Melanoma") . -- si on veut reproduite l'instance EXACTE du graphe
 
  ?target rdfs:label ?targetname . -- pour que ça soit plus lisible
  ?moa rdfs:label ?moaname . -- pour que ça soit plus lisible
  
  
}


-- 7

SELECT * WHERE {
  ?mAb imgt:inn_name ?name.
  ?mAb imgt:hasClinicalIndication imgt:Solid_tumors .

}



