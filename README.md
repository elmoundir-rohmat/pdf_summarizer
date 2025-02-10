Résumeur de PDF avec Streamlit et OpenAI
Cette application permet de télécharger un fichier PDF, d'en extraire le texte, puis de générer un résumé concis en utilisant l'API OpenAI.

🚀 Fonctionnalités
Téléchargement de PDF : Chargez votre fichier PDF directement dans l'application.
Extraction de texte : Le texte est extrait automatiquement du PDF.
Génération de résumé : Obtenez un résumé concis du texte extrait grâce à l'API OpenAI.
🛠️ Installation
Cloner le dépôt :

bash
Copier
Modifier
git clone https://github.com/votre-utilisateur/votre-repo.git
cd votre-repo
Créer un environnement virtuel :

bash
Copier
Modifier
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate
Installer les dépendances :

bash
Copier
Modifier
pip install -r requirements.txt
Configurer les variables d'environnement :

Créez un fichier .env à la racine du projet.

Ajoutez votre clé API OpenAI :

ini
Copier
Modifier
OPENAI_API_KEY="votre_clé_api"
🖥️ Utilisation
Lancer l'application Streamlit :

bash
Copier
Modifier
streamlit run main.py
Interagir avec l'application :

Ouvrez votre navigateur à l'adresse indiquée (généralement http://localhost:8501).
Téléchargez un fichier PDF.
Cliquez sur "Générer le résumé" pour obtenir le résumé du document.
📋 Fichiers du projet
main.py : Script principal contenant l'interface Streamlit.
extract_from_pdf.py : Module pour l'extraction du texte des PDF.
summarize_from_pdf.py : Module pour la génération du résumé en utilisant l'API OpenAI.
requirements.txt : Liste des dépendances Python nécessaires.
.env : Fichier contenant la clé API OpenAI (à créer par l'utilisateur).