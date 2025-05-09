import openai

def analyse_contrat_assurance(text, api_key):
    # Créer un client OpenAI avec la clé API
    client = openai.OpenAI(api_key=api_key)

    # Appeler l'API de ChatGPT avec le contexte d'expert en assurance
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un expert en assurance avec 20 ans d'expérience dans l'analyse des contrats. Tu analyses méthodiquement les documents pour en extraire les informations clés."},
            {"role": "user", "content": f"""Analyse ce contrat d'assurance et :
1. Détermine si l'assuré est bien couvert (en considérant les exclusions et limites)
2. Liste les couvertures principales avec leurs garanties et montants
Texte du contrat: {text}

Réponds en français avec cette structure:
**Niveau de Couverture:**
- [Analyse détaillée des protections et risques résiduels]

**Récapitulatif des Garanties:**
- [Liste organisée des couvertures avec détails techniques]"""}
        ],
        max_tokens=500,  # Augmentation pour permettre une analyse complète
        temperature=0.3  # Pour des réponses plus factuelles et précises
    )

    return response.choices[0].message.content