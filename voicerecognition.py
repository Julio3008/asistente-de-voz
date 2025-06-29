import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import os
import uuid

recognizer = sr.Recognizer()

def hablar(texto):
    tts = gTTS(text=texto, lang='es')
    filename = f"voz_{uuid.uuid4()}.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def escuchar():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {texto}")
        return texto.lower()
    except:
        print("No entendí lo que dijiste.")
        return ""

# Saludo inicial
hablar("Hola, ¿a qué página vamos hoy día?")
comando = escuchar()

if 'amazon' in comando:
    hablar('¿Qué quieres comprar en Amazon?')
    busqueda = escuchar()
    webbrowser.open(f'https://www.amazon.es/s?k={busqueda}')
