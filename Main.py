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
    st.title("Résumeur de PDF")
    st.write("Charge un fichier PDF et obtiens un résumé en quelques secondes.")

    # Upload du fichier PDF
    uploaded_file = st.file_uploader("📂 Télécharge un fichier PDF", type="pdf")

    # Vérifier si un fichier a été uploadé
    if uploaded_file:
        st.info("📂 Analyse du fichier en cours...")

        # Lire le fichier PDF sous forme de bytes
        with st.spinner("📜 Extraction du texte..."):
            text = extract_text_from_pdf(uploaded_file)  # Correction pour lire le fichier

        if text.strip():  # Vérifie si du texte a été extrait
            st.subheader("📜 Texte extrait du PDF")
            st.text_area("🔍 Aperçu du texte extrait", text, height=200)

            # Bouton pour générer le résumé
            if st.button("📄 Générer le résumé") and api_key:
                with st.spinner("💡 Génération du résumé..."):
                    summary = summarize_pdf_text(text, api_key)

                st.subheader("📝 Résumé du document")
                st.write(summary)
        else:
            st.warning("⚠️ Aucun texte n'a été extrait du PDF. Vérifie que le fichier contient bien du texte, ou qu'il ne s'agit pas d'un fichier mal scanné.")

if __name__ == "__main__":
    main()
