import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning")

    elif hour>=12 and hour<18 :
        speak("Good Afternoon")

    else: 
        speak("Good Evevning")
    speak("Hello Ashish. I am Jarvis. How may I help you")

def takeCommand():   # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.8
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Say that again Please...")
            return "None"
        return query    
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Please wait I am Searching...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        #elif 'play music'in query:
            #music_dir=""
            #songs=os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codePath ="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open chrome' in query:
            chromePath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        elif 'open zoom' in query:
            zoomPath ="C:\\Users\\hp\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)   



