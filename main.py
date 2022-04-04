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
from googletrans import Translator


def assistant_voix(sortie):
    if sortie!=None:
        voix=pyttsx3.init()
        voix.setProperty('voice',"french")
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
        else:
            try:
                vocal=r.recognize_sphinx(audio,language="fr-fr")
                print(vocal)
            except:
                assistant_voix(pas_compris)

def application(entree):
    if entree!=None:
        dio_apps={
            "note":["notepad","note pad"],
            "sublime":["sublime text","sublime texte"],
            "obs":["obs","capture de l'écran"],
            "google":["google"]


        }
        fini=False
        while not fini:
            for x in dio_apps["note"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de notepad")
                    fini=True
            for x in dio_apps["sublime"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de sublime")
                    fini=True
            for x in dio_apps["google"]:
                if x in entree.lower():
                    assistant_voix("Google")
                    fini=True

def calcul(entree):
    if entree!=None:
        traducteur=Translator()
        traduction=traducteur.translate(text=entree,dest="en").text
        app_id="PLACEZ VOTRE IDEE ICI"
        client=wolframalpha.Client(app_id)
        res=client.query(traduction)
        try:
            reponse=next(res.results).text
            traduction_reponse=traducteur.translate(text=reponse,dest='fr').text
            assistant_voix("Le résultat est : "+traduction_reponse)
        except:
            assistant_voix("Il y a eu une erreur ,désolé")
def sur_le_net(entree):
    if entree!=None:
        if "youtube" in entree.lower():
            indx=entree.lower().split.index("youtube")
            recherche=entree.lower().split()[indx+1:]
            if len(recherche)!=0:
                assistant_voix("Recherche sur youtube")
                webbrowser.open("http://www.youtube.com/results?search_query="+"+".join(recherche),new=2)
        elif "wikipédia" in entree.lower():
            wikipedia.set_lang("fr")
            try:
                indx = entree.lower().split.index("wikipédia")
                recherche = entree.lower().replace("cherche sur wikipédia","")
                if len(recherche)!=0:
                    resultat=wikipedia.summary(recherche,sentences=1)
                    assistant_voix("Recherche sur Wikipédia .")
                    assistant_voix(resultat)
            except:
                assistant_voix("Désolé ,aucune page n'a été trouvé")
        else:
            if "google" in entree.lower():
                indx=entree.lower().split().index("google")
                recherche=entree.lower().split()[indx+1:]
                if len(recherche)!=0:
                    assistant_voix("Recherche sur Google")
                    webbrowser.open("http://www.google.com/search?q="+"+".join(recherche),new=2)
            elif "cherhe" in entree.lower():
                indx=entree.lower().split().index("cherche!")
                recherche=entree.lower().split()[indx+1:]
                if len(recherche)!=0:
                    assistant_voix("Recherche sur Google")
                    webbrowser.open("http://www.google.com/search?q="+"+".join(recherche),new=2)
            elif "recherhe" in entree.lower():
                indx=entree.lower().split().index("recherche!")
                recherche=entree.lower().split()[indx+1:]
                if len(recherche)!=0:
                    assistant_voix("Recherche sur Google")
                    webbrowser.open("http://www.google.com/search?q="+"+".join(recherche),new=2)


def main():
    assistant_voix("Bonjour monsieur, je suis votre assistant de Bureau.Dites- moi ce que je peux faires pour vous")
    fermer=["arretes-toi","tais-toi"]
    ouvrir=["ouvrir","peux-tu ouvrir"]
    cherche=["cherche sur youtube","cherche sur google","cherche sur wikipedia","cherche","peux-tu faire cette recherche"]
    calculs=["calcule la somme de","calcule la différence de","calcule le produit de ","calcule","fais moi l'opération","calcule"]
    actif=True
    while actif:
        if (entree:= reconnaissance()) is not None:
            for x in range(len(fermer)):
                if fermer[x] in entree.lower():
                    assistant_voix("A la prochaine monsieur")
                    actif=False
            for x in range(len(ouvrir)):
                if ouvrir[x] in entree.lower():
                    application(entree)
                    break
            for x in range(len(cherche)):
                if cherche[x] in entree.lower():

                    sur_le_net(entree)
                    break
            for x in range(len(calculs)):
                if calculs[x] in entree.lower():
                    calcul(entree)
                    break
main()

