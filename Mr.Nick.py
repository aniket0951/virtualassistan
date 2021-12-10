import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzning.....")
        query = r.recognize_google(audio,language='en-in')
        speak(query)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please!")
        return None
    return query

takeCommand()
