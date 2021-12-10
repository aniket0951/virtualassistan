import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import re
import geocoder
import phonenumbers
from phonenumbers import geocoder, carrier

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")


# engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.setProperty("language", 'hi-In')
    engine.say(text)
    engine.runAndWait()


global command


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Mr.Nick" in command:
                command = command.replace("Mr.Nick")
            return command

    except:
        pass


def run_alexa():
    command = take_command()
    print(command)
    try:
        if "nick" in command:
            if "play" in command:
                song = command.replace("play", "")
                talk("playing" + song)
                pywhatkit.playonyt(song)
            elif "time" in command:
                time = datetime.datetime.now().strftime("%H:%M")
                talk("The current time is " + time)
            elif "who is" in command:
                person = command.replace("who is", "")
                info = wikipedia.summary(person, 1)  # how many lines do I want in the summary
                talk(info)
            elif "tell me a joke" in command:
                talk(pyjokes.get_joke())
            elif "stock" in command:
                stock_price = pywhatkit.search(command)
                talk(stock_price)
            elif "stop" in command:
                talk("alexa is going down")
            elif "network" in command:
                return wifiNetwork()
            elif "service provider" in command:
                myNumb = []
                for numb in command.split():
                    if numb.isdigit():
                        myNumb.append(numb)
                search_num = listToString(myNumb)
                talk(f"I am going the search a service provider of {search_num}")
                return getServiceProvider(myNumb)
            elif "about your self" in command:
                return introducedSelf()
            elif "android studio" in command:
                return openMyApplication("android")
            elif "visual studio" in command or "vs code" in command:
                return openMyApplication("vscode")
            elif "notepad" in command:
                return openMyApplication("notepad")
            elif "whatsapp" in command:
                return openMyApplication("whatsapp")
            elif "chrome" in command:
                return openMyApplication("chrome")
            elif "postman" in command:
                return openMyApplication("postman")
            elif "filezila" in command:
                return openMyApplication("filezila")
            elif "write a note" in command:
                return writeNote()
            elif "show note" in command:
                talk("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                talk(file.read(6))
            elif "i love you" in command:

                talk("It's hard to understand")
            else:
                talk("Please say the command again.")
        else:
            print("Mr nick is not in command")
    except:
        pass


def wifiNetwork():
    command_output = subprocess.run(["netsh", "wlan", "show", "network", ], capture_output=True).stdout.decode()

    network_names = (re.findall("SSID (.*)\r", command_output))
    if network_names:
        count = len(network_names)
        talk(f"Hey mister user there are a {count}   wifi network available.")
        talk(" ")
        talk(network_names)
    else:
        talk("Sorry there is no any wifi network available.")


def getServiceProvider(number):
    search_num = listToString(number)
    count_num = len(search_num)
    print(f"count of number {count_num}")
    if count_num == 10:
        phoneNumber = phonenumbers.parse(f"+91{search_num}")
        Carrier = carrier.name_for_number(phoneNumber, 'en')
        Region = geocoder.description_for_number(phoneNumber, 'en')

        if Carrier and Region:
            talk(f"The service provider of this number is a {Carrier}  and the is from {Region}")
        else:
            talk("Sorry i am not able to search foreign number.. please give me a indian number")
    else:
        talk("You  are  giving  a  invalid  number  please  give  me  a  valid  number")


# --- introduced my self
def introducedSelf():
    talk("Hi ")
    talk("My  name  is Nick. I born in 2021 by Aniket Suryawanshi.")
    talk("I am the Assistant of Aniket Suryawanshi")


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


# -- open desktop ApplicationStage
def openMyApplication(name):
    if name == "android":
        talk("Opening Android Studio")
        subprocess.call('C://Program Files//Android//Android Studio//bin//studio64.exe')
    elif name == "notepad":
        talk(f"Opening {name}")
        subprocess.call('notepad.exe', shell=True)
    elif name == "whatsapp":
        talk(f"Opening {name}")
        subprocess.call('C://Users//anike//AppData//Local//WhatsApp//WhatsApp.exe')
    elif name == "chrome":
        talk(f"Opening {name}")
        subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
    elif name == "vscode":
        talk(f"Opening {name}")
        subprocess.call('C://Users//anike//AppData//Local//Programs//Microsoft VS Code//Code.exe')
    elif name == "postman":
        talk(f"Opening {name}")
        subprocess.call('C://Users//anike//AppData//Local//Postman//Postman.exe')
    elif name == "filezila":
        talk(f"Opening {name}")
        subprocess.call('C://Program Files (x86)//FileZilla FTP Client//filezilla.exe')
    else:
        talk("sorry i am not able to find your application")

# --- write the note
def writeNote():
    talk("What should i write, sir")
    note = take_command()
    file = open('jarvis.txt', 'w')
    talk("Sir, Should i include date and time")
    snfm = take_command()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)

while True:
    run_alexa()
