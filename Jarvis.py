#Author : Shraddha Mane 
#Program language : python
'''
before running the program install the below packages...

pip install wikipedia
pip install pyttsx3
pip intall pypwin32
pip install speechRecognition
'''

import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os           #for playing music

engine= pyttsx3.init('sapi5')    #for taking voice
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)   #for David voice (male vioce) ,for female voice use voices[1]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good Morning!")

    elif hour>=12 and hour>=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Mam. Please tell me how may i help you?")

def takeCommand():
    #it takes microphone input from the user and returns string output.
    r=sr.Recognizer()   #helps in Recognizing audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1      ## seconds of non-speaking audio before a phrase is considered complete
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"User Said:  {query}\n")

    except Exception as e:
     #   print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()             #converting command to lowercase to compute further
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/...")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/...")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com/...")

        elif 'play music' in query:
            music_dir = "D:\\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath="C:\\Users\\Anand Computers\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'show pictures' in query:
            Ipath="C:\\Users\\Anand Computers\\Pictures\\Saved Pictures"
            os.startfile(Ipath)

        elif 'open calculator' in query:
            Cpath="C:\\Windows\\System32\\calc.exe"
            os.startfile(Cpath)

        elif 'take screenshot' in query:
            Tspath="C:\\Windows\\System32\\SnippingTool.exe"
            os.startfile(Tspath)

        elif 'open notepad' in query:
            Npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(Npath)

        elif 'open paint' in query:
            Mpath="C:\\Windows\\System32\\mspaint.exe"
            os.startfile(Mpath)
            
        elif 'your name' in query:
            speak("My Real name is David. But Shraddha mam and all users call me Jarvis.. How can I help you?")
        
        elif 'thank you'  in query:
            speak("Welcome. It was my pleasure to help you..! If you have any more questions or need assistance with anything else ,don't hesitate to ask..I am here to help! Have a great day!")
        
        elif 'quit' in query:
            speak("Sure! If you have any more questions ,dont hesitate to ask..I am here to help! Have a great day! Bye.!")
            exit(0)


'''
Sample voice input : open google              or
                     open you tube            or
                     open paint               or
                     computer organization according to wikipedia
'''



        
        
        
            
