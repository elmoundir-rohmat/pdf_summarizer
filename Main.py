from dotenv import load_dotenv
import streamlit as st
import os
import openai
from extract_from_pdf import extract_text_from_pdf
from summarize_from_pdf import summarize_pdf_text

# Charger les variables d'environnement
load_dotenv()

# Récupérer la clé API
api_key = os.getenv("OPENAI_API_KEY")


def main():
    """Interface principale Streamlit pour résumer un PDF."""
    st.title("📄 Résumeur de PDF")
    st.write("Charge un fichier PDF et obtiens un résumé en quelques secondes.")


    # Upload du fichier PDF
    uploaded_file = st.file_uploader("📂 Télécharge un fichier PDF", type="pdf")

    if uploaded_file and api_key:
        st.info("📂 Analyse du fichier en cours...")

        # Extraction du texte
        with st.spinner("📜 Extraction du texte..."):
            text = extract_text_from_pdf(uploaded_file)

        st.subheader("📜 Texte extrait du PDF")
        st.text_area("🔍 Aperçu du texte extrait", text, height=200)

        # Résumé avec OpenAI
        if st.button("📄 Générer le résumé"):
            with st.spinner("💡 Génération du résumé..."):
                summary = summarize_pdf_text(text, api_key)

            st.subheader("📝 Résumé du document")
            st.write(summary)

if __name__ == "__main__":
    main()