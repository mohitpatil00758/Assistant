import subprocess
import sys
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

try: import speech_recognition as sr
except :
    install("speech_recognition")
    import speech_recognition as sr
try:import pyttsx3
except: 
    install("pyttsx3")
    import pyttsx3
try:import datetime
except:
    install("datetime")
    import datetime
try:import wikipedia as wiki
except:
    install("wikipedia")
    import wikipedia as wiki
try:from PyDictionary import PyDictionary
except:
    install("PyDictionary")
    from PyDictionary import PyDictionary
try:import google
except:
    install("google")
    import google
try:import webbrowser
except:
    install("webbrower")
    import webbrowser
try : import PyPDF2
except:
    install("PyPDF2")
    import PyPDF2


    install("nltk")
    import nltk

dictionary=PyDictionary()
engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
for i in voices:
    print(i.id)

engine.setProperty('voice',voices[1].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(name):
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12 :
        speak("Good morning")

    elif hour>= 12 and hour<=17:
        speak("Good Afternoon")

    else:
        speak("Good Evening")


    speak("Hello "+name+"! friday is Online")
    return name

def takevoice() :

    # speechtoText

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"{query}\n")
    except Exception as e:
        print(e)

        print("Say that again...")

        return "none"
    return query

def askname():
    speak("May I ask Whom I am talking to")
    name  = takevoice().lower()
    return name
if __name__ == "__main__":
    name = wishme(askname())
    while True:
        query = takevoice().lower()
        if "hello friday" in query:
            speak("Hello "+name+" How may I help you")
        
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            speak("Searching"+query+"in Wikipedia")
            results = wiki.summary(query, sentences=2)
            speak(" According to Wiki!")
            print(f"{results}\n")
            speak(results)

        elif "what does" in query:
            query = query.replace("what does ", "")
            query = query.replace(" mean","")
            print(query)
            dictionary=PyDictionary()
            meaning = dictionary.meaning(query)
            speak(query+ "Means")
            print(f"{meaning}\n")
            speak(meaning)
        elif "google" in query:
            query = query.replace("google ", "https://www.google.com/search?q=")
            ##from googlesearch import search
            ##for j in search(query ,tld='com', lang='en', num=10, start=0, stop=None, pause=2.0): 
            ##    print(j) 
            ##    speak(j)
            print(query)
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            webbrowser.register('FireFox', None,webbrowser.BackgroundBrowser(firefox_path),1)
            webbrowser.get(using='FireFox').open_new(query)
        
        elif "open" in query:
            query = query.replace("open ", "")
            print(query)
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            opera_path = "C:\\Program Files\\Opera\\launcher.exe"
            if "firefox" in query:
                 query = query.replace("in firefox","")
                 webbrowser.register('FireFox', None,webbrowser.BackgroundBrowser(firefox_path),1)
                 webbrowser.get(using='FireFox').open_new(query)
            
        elif "what's time" in query:
            speak("Time is"+datetime.datetime.now().strftime("%H:%M"))

        elif "what is time" in query:
            speak("Time is"+datetime.datetime.now().strftime("%H:%M"))
        
        elif "today's date" in query:
            speak("today's date is"+datetime.datetime.today().strftime("%B %d, %Y"))
        
        elif "thank you friday"== query:
            speak("You're most welcome "+name)
            speak("Is there anything I can help ypu with")
        elif "friday"==query:
            speak("Yes?")

        elif "bye-bye"== query:
            speak("Bye "+name+"...")
            exit()    

        elif "on youtube" in  query and "search" in query:
            query = query.replace(" on youtube","")
            
            query = query.replace("search", "https://www.youtube.com/results?search_query=")
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            webbrowser.register('FireFox', None,webbrowser.BackgroundBrowser(firefox_path),1)
            webbrowser.get(using='FireFox').open_new(query)
            
        else:
            if query !=  "none":
                dictionary=PyDictionary()
                meaning = dictionary.meaning(query)
                speak(query+ "Means")
                print(f"{meaning}\n")
                speak(meaning)
        
    