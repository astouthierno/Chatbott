
import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections



# Assurez-vous que les ressources nécessaires sont téléchargées
nltk.download('punkt')

# Exemple de paires pour le chatbot
pairs = [
    [
        r"bonjour|salut|coucou",
        ["Bonjour ! Comment puis-je vous aider ?", "Salut ! Que puis-je faire pour vous aujourd'hui ?"]
    ],
    [
        r"(.*) ton nom (.*)?",
        ["Je suis un chatbot voco-textuel. Et vous ?"]
    ],
    [
        r"(.*) temps (.*)?",
        ["Je ne peux pas vérifier le temps, mais il fait toujours beau ici dans mon monde numérique."]
    ],
    [
        r"merci|merci beaucoup",
        ["Avec plaisir !", "N'hésitez pas si vous avez d'autres questions."]
    ],
    [
        r"au revoir|bye",
        ["Au revoir ! Passez une excellente journée."]
    ]
]

# Créez le chatbot
chatbot = Chat(pairs, reflections)

# Fonction pour la reconnaissance vocale
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Parlez maintenant...")
        try:
            audio = recognizer.listen(source, timeout=5)
            st.info("Transcription en cours...")
            text = recognizer.recognize_google(audio, language="fr-FR")
            return text
        except sr.UnknownValueError:
            st.error("Je n'ai pas pu comprendre ce que vous avez dit. Veuillez réessayer.")
        except sr.RequestError as e:
            st.error("Le service de reconnaissance vocale est indisponible : {e}")
        except Exception as ex:
            st.error(f"Erreur : {ex}")
    return None
background_image = "c:\\Users\\Easy Services Pro\\Documents\\ALBG\\Site web\\New logos\\AICHA.png"
  # Lien vers l'image locale

page_bg_img = '''
<style>
.stApp {
#background-image: url("");
background: linear-gradient(0.25turn, #3f87a6, #ebf8e1, #f69d3c);
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Code CSS pour ajouter l'image d'arrière-plan
st.markdown(
    f"""
    <style>

    .reportview-container {{
        background-image: url({background_image});
        background-size: cover;
        background-position: center;
        height: 100vh;
        color: white;
    }}
    .sidebar .sidebar-content {{
        background-color: rgba(0, 0, 0, 0.5);
    }}
    </style>
    """, unsafe_allow_html=True
)


# Application Streamlit
st.title("Chatbot à commande vocale")
st.write("Interagissez avec le chatbot via du texte ou de la parole.")

# Options d'entrée
input_type = st.radio("Choisissez un mode d'entrée", ("Texte", "Voix"))



if input_type == "Texte":
    user_input = st.text_input("Écrivez ici :")
    if st.button("Envoyer"):
        if user_input:
            response = chatbot.respond(user_input)
            st.write("Chatbot :", response)
        else:
            st.warning("Veuillez entrer un message.")

elif input_type == "Voix":
    if st.button("Parler"):
        user_input = recognize_speech()
        if user_input:
            st.write("Vous avez dit :", user_input)
            response = chatbot.respond(user_input)
            st.write("Chatbot :", response)

