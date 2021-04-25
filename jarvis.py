import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("this is jarvis ai assitant")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def wishme():
    speak("welcome back sir!")
    speak("the current time is")
    time()
    speak("Jarvis at your service Please tell me how i can help you?")
    
wishme()

def takeCommand():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizning")
        query = r.recognize_google(audio, language= 'en-in')

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query

takeCommand()