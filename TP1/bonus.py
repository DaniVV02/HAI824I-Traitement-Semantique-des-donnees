import requests

# Texte d'exemple
texte = """Wolfgang Amadeus Mozart, né à Salzbourg le 27 janvier 1756, mort à Vienne, la capitale
autrichienne, le 5 décembre 1791, est un compositeur. Il est fils de Léopold Mozart et était marié à
Constance Weber. Parmi ses œuvres les plus célèbres, on trouve l'opéra “La flûte enchantée” et la
41 Symphonie en ut majeur, dite “Jupiter”. Cette symphonie est composée de 4 parties : 1. Allegro
Vivace, 2. Andante Cantabile, 3. Menuetto, 4. Molto Allegro. Elle a été enregistrée par l'orchestre
symphonique de Londres sous la direction de Claudio Abbado en 1980."""

# URL de l'API DBpedia Spotlight
url = "https://api.dbpedia-spotlight.org/fr/annotate"

# Paramètres de la requête
params = {
    "text": texte,
    "confidence": 0.5  # Confiance minimale pour considérer une entité
}

# En-têtes
headers = {
    "Accept": "application/json"
}

# Envoi de la requête
response = requests.get(url, params=params, headers=headers)

# Vérification de la réponse
if response.status_code == 200:
    data = response.json()
    print("\n🔹 **Résultats DBpedia Spotlight** 🔹\n")
    for entity in data.get("Resources", []):
        print(f"🔗 {entity['@surfaceForm']} → {entity['@URI']}")
else:
    print("Erreur lors de l'accès à DBpedia Spotlight :", response.status_code)
