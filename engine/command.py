import pyttsx3
import speech_recognition as sr
import eel
import time
from datetime import datetime
import pyautogui
from engine.config import ASSISTANT_NAME

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 140)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def get_time_greeting():
    current_time = datetime.now().time()
    if current_time.hour < 6:
        return "Working late night"
    elif current_time.hour < 12:
        return "Good Morning"
    elif 12 <= current_time.hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"
    

def takecommand():
   
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening......')
        eel.DisplayMessage('Listening......')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

    try:
        print('Recognizing.....')
        eel.DisplayMessage('Recognizing......')
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        # speak(query)
        # eel.ShowHood()
    except Exception as e:
        return ""
    
    return query.lower()

# text = takecommand()
        
# speak(text)
import time

@eel.expose
def allCommands():
    #  greeting
    time_greeting = get_time_greeting()
    speak(time_greeting + " Sir")
    
    lock = 1
    count = 0
    while True:
        query = takecommand()
        print(query)
        if "wake up" in query:
            lock = 1
            speak("At your service , sir.")
            count = 0
            continue 
        if lock:
            if "open" in query:
                from engine.features import openCommand
                openCommand(query)
            elif "close" in query:
                from engine.features import closeAppWeb
                closeAppWeb(query)
            elif "search" in query:
                from engine.features import searchCommand
                searchCommand(query)
            elif "on youtube" in query and "play" in query:
                from engine.features import PlayYoutube
                PlayYoutube(query)
            elif "pause" in query:
                pyautogui.press("k")
            elif "play" in query:
                pyautogui.press("k")
            elif "mute" in query:
                pyautogui.press("m")
            elif "unmute" in query:
                pyautogui.press("m")
            elif "full screen" in query:
                pyautogui.press("f")
            elif "subtitle on" in query:
                pyautogui.press("c")
            elif "minimise video" in query or "minimize video" in query:
                pyautogui.press("i")
            elif "expand video" in query:
                pyautogui.press("i")
            elif "theatre mode" in query or "theatre mod" in query:
                pyautogui.press("t")
            elif "volume up" in query:
                from engine.features import volumeUp
                volumeUp()
            elif "volume down" in query:
                from engine.features import volumeDown
                volumeDown()
            elif "next video" in query:
                from engine.features import playNext
                playNext()
            elif "move" in query:
                from engine.features import moveFB
                moveFB(query)
            elif "previous video" in query:
                from engine.features import playPrevious
                playPrevious()
            elif "temperature" in query or "weather" in query:
                from engine.features import weather
                weather(query)
            elif "the time" in query:
                strTime = datetime.now().strftime("%H:%M")
                print(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")
            elif "go to sleep" in query or "sleep "+ASSISTANT_NAME in query:
                speak("See you later Master") 
                eel.ShowHood()
                exit()
            elif "hold" in query:
                lock = 0
                speak("You can call me anytime.")
            elif "remember that" in query or "remembered that" in query:
                from engine.features import rememberFunction
                rememberFunction(query)
            elif "what do you remember" in query:
                from engine.features import rememberCheck
                rememberCheck()
            elif "set an alarm" in query:
                print("Input time example :- 12 and 12 and 12")
                speak("Set the time")
                a = input("Please tell me the time :- ")
                from engine.features import alarm
                alarm(a)
            else:
                count += 1  # Increment count
                if count == 3:
                    lock = 0 
                speak("Try again" + (" Later" if count == 3 else ""))
            # Add a delay to prevent continuous loop iteration without pause
            time.sleep(1)
        
    # eel.ShowHood()
