import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import smtplib
import aiml


# confs for pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']

engine.setProperty('voice', voices[7].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour <= 12:
        speak("Good Morning Sir!!")
    elif hour <= 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Alexis. Please tell me how may I help you?")


def takeCommand():
    ''' It takes microphone input from the user and returns string output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....\n")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.energy_threshold = 180
    try:
        print("Recognizing...\n")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        speak("Say that again please...\n")
        return "None"  # None string will be returned

    return query


def takeCommandAlexis():
    ''' It takes microphone input from the user and returns string output '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....\n")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.energy_threshold = 150
    try:
        print("Recognizing...\n")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        
        return "None"  # None string will be returned

    return query


def emailMessage(content, to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('testingsharma78@gmail.com', 'tanvos-duxPe0-dubzew')
    server.sendmail('testingsharma78@gmail.com', to, content)
    server.close()
    

list = []


contacts = {"father":"pcpandey1965@gmail.com",
            "friend1":"satyam2507mishra@gmail.com",
            "friend2":"rahulrana@outlook.com",
            "myself": "jjustin.john98@gmail.com"}

if __name__ == "__main__":
    wishMe()
        
    flag = 1
    while flag:
        query = takeCommand().lower()
        print(query)
        flag = 1
        if query in terminate:
            print("Until next time...")
            speak("Until next time...")
            break
        
        if 'what can you do' in query:
            speak("I can search something for you on Google, open Youtube or Twitter.")
            speak("I can tell you a joke if you want to lighten your mood or we can have a talk.")
            speak("I can email someone or play music")
            speak("So......... tell me what would you like me to do?")
            
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab('http://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open_new_tab('http://www.google.com')

        elif 'open twitter' in query:
            webbrowser.open_new_tab('http://www.twitter.com')

        elif 'play music' in query:
            subprocess.call(
                ["afplay", "/Users/devangpandey/Desktop/Alexis/Humdard.mp3"])

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            
            hour = int(datetime.datetime.now().hour)
            if hour>=12 and hour<16:
                speak(f"Sir, the time is {strTime}. Good Afternoon!")
            
            elif hour>0 and hour<12:
                speak(f"Sir, the time is {strTime}. Good Morning!")
            
            else:
                speak(f"Sir, the time is {strTime}. Good Evening!")
                
        elif 'photos' in query:        
            os.system("open /System/Applications/Photos.app")
            
        elif 'sad' in query:
            speak("Sir, Maybe a joke might help?")
            speak("What is the most shocking city in the world?")
            speak("Electicity. ")  
        
        elif 'joke' in query:
            speak("Why couldn't the bicycle stand up on it's own?")
            speak("It was too tired. ")       
            
        elif 'email' in query:
            try:
                speak("Who should I send it to?")
                temp = takeCommand()
                to = contacts[temp]
                speak("What should I say?")
                content = takeCommand()
                emailMessage(content, to)

                speak("Email has been sent!!")
            except:
                speak("Sorry the email was not sent!")  
                
        elif 'search youtube' in query:
            speak("What would you like to search")
            term = takeCommand()
            new = 2 
            tabUrl = "https://www.youtube.com/results?search_query="
             
            if term !="none":
                webbrowser.open(tabUrl+term,new=new)
        
        elif 'search' in query:
            speak("What would you like to search")
            term = takeCommand()
            new = 2 
            tabUrl = "https://www.google.com/search?q="
             
            if term !="none":
                webbrowser.open(tabUrl+term,new=new)
                
        elif 'talk' in query:
            kernel = aiml.Kernel()

            if os.path.isfile("bot_brain.brn"):
                kernel.bootstrap(brainFile="bot_brain.brn")
            else:
                kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
                
                #kernel.saveBrain("bot_brain.brn")
                
            input_text = "load aiml b"
            kernel.respond(input_text)
                
            speak("Yeah! Let's talk")
            while True:
                input_text = takeCommandAlexis()
                if input_text in terminate:
                    print('Until next time...')
                    speak('Until next time...')
                    exit()
                
                response = kernel.respond(input_text)
                
                print ("A.L.E.X.I.S: " + response)
                speak(response) 
                
        
        speak("Do you want me to do anything else?")
        answer = takeCommand()
        if 'no' in answer:
            speak("See you later gater")
            flag = 0              
                          
                    
                
                
