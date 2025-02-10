import openai

def summarize_pdf_text(text, api_key):
    # Créer un client OpenAI avec la clé API
    client = openai.OpenAI(api_key=api_key)

    # Appeler l'API de ChatGPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # ou "gpt-4" si disponible
        messages=[
            {"role": "system", "content": "Tu es un assistant utile qui résume des documents."},
            {"role": "user", "content": f"Résume ce texte en quelques phrases : {text}"}
        ],
        max_tokens=150  # Limite la longueur du résumé
    )

    # Récupérer le résumé
    summary = response.choices[0].message.content
    return summary

