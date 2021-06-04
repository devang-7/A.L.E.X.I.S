import pyttsx3

import speech_recognition as sr

from gtts import gTTS



# confs for pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in range(20):
    print(voices[i].id)
engine.setProperty('voice', voices[7].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour <= 12:
#         speak("Good Morning!!")
#     elif hour <= 16:
#         speak("Good Afternoon")
#     else:
#         speak("Good Evening")

#     speak("Hello Sir! I am Alex. Please tell me how may I help you?")


# def takeCommand():
#     ''' It takes microphone input from the user and returns string output '''
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening.....\n")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#         r.energy_threshold = 150
#     try:
#         print("Recognizing...\n")
#         # Using google for voice recognition.
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")  # User query will be printed.

#     except Exception as e:
#         # print(e)
#         # Say that again will be printed in case of improper voice
#         speak("Say that again please...\n")
#         return "None"  # None string will be returned

#     return query


# def emailMessage(content, to):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('testingsharma78@gmail.com', 'tanvos-duxPe0-dubzew')
#     server.sendmail('testingsharma78@gmail.com', to, content)
#     server.close()
    

# if __name__ == "__main__":
#     wishMe()

#     while True:
#         query = takeCommand().lower()
#         print(query)
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=1)
#             speak("According to wikipedia ")
#             print(results)
#             speak(results)

#         elif 'open youtube' in query:
#             webbrowser.open_new_tab('http://www.youtube.com')

#         elif 'open google' in query:
#             webbrowser.open_new_tab('http://www.google.com')

#         elif 'open twitter' in query:
#             webbrowser.open_new_tab('http://www.twitter.com')

#         elif 'play music' in query:
#             subprocess.call(
#                 ["afplay", "/Users/devangpandey/Desktop/Alexis/Humdard.mp3"])

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            
#             hour = int(datetime.datetime.now().hour)
#             if hour>=12 and hour<16:
#                 speak(f"Sir, the time is {strTime}. Good Afternoon!")
            
#             elif hour>0 and hour<12:
#                 speak(f"Sir, the time is {strTime}. Good Morning!")
            
#             else:
#                 speak(f"Sir, the time is {strTime}. Good Evening!")
                
#         elif 'photos' in query:        
#             os.system("open /System/Applications/Photos.app")
            
#         elif 'sad' in query:
#             speak("Sir, Maybe a joke might help?")
#             speak("What is the most shocking city in the world?")
#             speak("Electicity. ")  
        
#         elif 'joke' in query:
#             speak("Why couldn't the bicycle stand up on it's own?")
#             speak("It was too tired. ")       
            
#         elif 'email' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "satyam2507mishra@gmail.com"
#                 emailMessage(content, to)

#                 speak("Email has been sent!!")
#             except:
#                 speak("Sorry the email was not sent!")    
                
# contacts = {"father":"pcpandey1965@gmail.com",
#             "friend":"satyam2507mishra@gmail.com"}
# print(contacts["father"])