#Importation
from urllib.request import urlopen
#from googletrans import translator
from random import choice
import subprocess
import webbrowser
import wolframalpha
import wikipedia
import pyttsx3
import speech_recognition as sr

#Code
def assistant_voix(sortie):
    if sortie!=None:
        voix=pyttsx3.init()
        print("A.I : "+sortie)
        voix.say(sortie)
        voix.runAndWait()
def internet():
    try:
        urlopen("https://www.google.com",timeout=1)
        return True
    except:
        return False

def reconnaissance():
    r=sr.Recognizer()
    pas_compris="Désolé, je n'ai pas compris"
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=0.7
        print("---")
        audio=r.listen(source)
        if internet():
            try:
                vocal=r.recognize_google(audio,language="fr-FR")
                print(vocal)
            except:
                assistant_voix(pas_compris)