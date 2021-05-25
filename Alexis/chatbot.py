import aiml
import os
kernel = aiml.Kernel()


if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
flag = 1
while True:
    if flag:
        input_text = "load aiml b"
        response = kernel.respond(input_text)
        print(response)
        flag = 0
    else:
        input_text = input(">Human: ")
        response = kernel.respond(input_text)
        print(response)

# import aiml
# import os
# import time
# import argparse 

# terminate = ['bye', 'buy', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']
           
# def listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Talk to J.A.R.V.I.S: ")
#         audio = r.listen(source)
#     try:
#         print r.recognize_google(audio)
#         return r.recognize_google(audio)
#     except sr.UnknownValueError:
#         speak(
#             "I couldn't understand what you said! Would you like to repeat?")
#         return(listen())
#     except sr.RequestError as e:
#         print("Could not request results from " +
#               "Google Speech Recognition service; {0}".format(e))


# if __name__ == '__main__':
#     args = get_arguments()

#     if (args.voice):
#         try:
#             import speech_recognition as sr
#             mode = "voice"
#         except ImportError:
#             print("\nInstall SpeechRecognition to use this feature." +
#                   "\nStarting text mode\n")
#     if (args.gtts):
#         try:
#             from gtts import gTTS
#             from pygame import mixer
#             voice = "gTTS"
#         except ImportError:
#             import pyttsx
#             print("\nInstall gTTS and pygame to use this feature." +
#                   "\nUsing pyttsx\n")
#     else:
#         import pyttsx

#     kernel = aiml.Kernel()

#     if os.path.isfile("bot_brain.brn"):
#         kernel.bootstrap(brainFile="bot_brain.brn")
#     else:
#         kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
#         # kernel.saveBrain("bot_brain.brn")

#     # kernel now ready for use
#     while True:
#         if mode == "voice":
#             response = listen()
#         else:
#             response = input("Talk to J.A.R.V.I.S : ")
#         if response.lower().replace(" ", "") in terminate:
#             break
#         jarvis_speech = kernel.respond(response)
#         print ("J.A.R.V.I.S: " + jarvis_speech)
#         speak(jarvis_speech)           