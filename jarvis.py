from ast import operator
from email.mime import audio
from re import A
from unittest import result
import pyttsx3
import speech_recognition as sr 
import webbrowser
import pyaudio
import wikipedia
import datetime
import os
import operator

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning CHARAN ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon CHARAN")
    else:
        speak("Good Evening sony")
    speak("I am trivrana . Tell me what can I do")

def takeComand():
    #it takes microphoen input  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognzing..")
        query = r.recognize_google(audio, language='en-in' )
        print(f" User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
        
    return query

if __name__== "__main__":
    wishme()
    while True:
        query = takeComand().lower()

        if 'wikipedia' in query:
            speak ('searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open VS code' in query:
            codePath = "C:\\Users\\DELL\\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
            
        elif 'open pycharm' in query:
            codePath = "C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm 2024.2.3.lnk"
            os.startfile(codePath) 
            
        elif 'open second disk' in query:
            codePath = "C:\\"
            os.startfile(codePath)
        
        elif 'do some calculations' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate")
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    'x' : operator.mul, #multiply
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("Result is")
            print(eval_binary_expr(*(my_string.split())))
            speak(eval_binary_expr(*(my_string.split())))
            
            
        
        
        
    