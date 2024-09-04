import os
import re
from playsound import playsound;
import eel
from engine.command import speak;
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
import wikipedia
import requests
from bs4 import BeautifulSoup
from engine.command import takecommand
from time import sleep
import pyautogui
import datetime
from pynput.keyboard import Key,Controller


# Playing AI sound function
@eel.expose
def playAssistentSound():
    music_dir = "www\\assets\\Audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)


#   SEARCHING

def searchCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query.lower()

    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google","")
        query = query.replace("search", "")
        query = query.replace("on", "")
        try:
            kit.search(query)
            result = googleScrap.summary(query,1)
            if(result!=""):
                speak("This is what I found on google")
                print(result)
                speak(result)
            else:
                raise Exception
        except Exception as e:
            speak("No speakable output available.")
    elif "wikipedia" in query:
        query = query.replace("search", "")
        query = query.replace("on", "")
        query = query.replace("wikipedia", "")
        try:
            answer = wikipedia.summary(query,sentences = 2)
            if(answer!=""):
                speak("According to wikipedia..")
                print(answer)
                speak(answer)
            else:
                raise Exception
        except Exception as e:
            speak("No speakable output available.")
    elif "on youtube" in query:
        query = query.replace("search", "")
        query = query.replace("on", "")
        query = query.replace("youtube", "")
        web = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(web)
        speak("These are the results.")
    else:
        speak("Try Again")



#   WEATHER
        
def weather(query):
    if "weather" in query:
        speak("Which city weather you want to know?")
    else:
        speak("Which city temperature you want to know?")
    query = takecommand()
    query = query.replace("tell","")
    query = query.replace("me","")
    query = query.replace("the","")
    query = query.replace("weather","")
    query = query.replace("temperature","")
    query = query.replace("in","")
    
    search = f"temperature in {query}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)

    if r.status_code == 200:
        data = BeautifulSoup(r.text, "html.parser")
        temp_element = data.find("div", class_="BNeawe")
        
        if temp_element:
            temp = temp_element.text
            speak(f"Current {search} is {temp}")
        else:
            speak("Temperature information not found on the page, Try again.")
    else:
        speak("No result found.")



#   OPEN and CLOSE Command
        
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if "mail" in query:
        speak("Opening mail")
        os.system('start "" "mailto:"')
    elif  "google chrome" in query or "chrome" in query:
        speak("Opening Google Chrome")
        os.system('start chrome')
    elif "notepad" in query:
        speak("Opening Notepad")
        os.system('start notepad')
    elif "vs code" in query or "visual studio" in query:
        speak("Opening vs code")
        vscode_path = r'D:\Apps\Visual Studio Code'
        os.system('start "" "' + vscode_path + '"')
    elif "code block" in query or "code blocks" in query:
        speak("Opening code blocks")
        code_block = r'D:\Apps\CodeBlocks'
        os.system('start "" "' + code_block + '"')
    elif "zoom" in query:
        speak("Opening Zoom")
        zoom = r'D:\Apps\Zoom'   
        os.system('start "" "' + zoom + '"')
    elif "fiver" in query or "fibre" in query:
        speak("Opening Fiverr")
        fiverr = r'D:\Apps\Fiverr'   
        os.system('start "" "' + fiverr + '"')
    elif "github" in query:
        speak("Opening github")
        github = r'D:\Apps\GitHub Desktop'   
        os.system('start "" "' + github + '"')
    elif "pycharm" in query:
        speak("Opening pycharm")
        pyCharm = r'D:\Apps\PyCharm'   
        os.system('start "" "' + pyCharm + '"')
    elif "explorer" in query:
        speak("Opening File Explorer")
        os.system('start explorer')
    elif "calculator" in query:
        speak("Opening Calculator")
        os.system('start calc')
    elif "google" in query:
        speak("Opening google")
        webbrowser.open("www.google.com")
    elif "youtube" in query:
        speak("Opening youtube")
        webbrowser.open("www.youtube.com")
    elif ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open ", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
         speak("not found")


def closeAppWeb(query):
    speak("Closing sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Tab closed")
    elif "two tabs" in query or "2 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("Both tabs closed")
    elif "three tabs" in query or "3 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "four tabs" in query or "4 tabs" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    else:
        query = query.replace("close","")
        query = query.replace(" ","")
        os.system(f"taskkill /f /im {query}.exe")


#   ALARM
         
def alarm(a):
      timehere = open("Alarmtext.txt","a")
      timehere.write(a)
      timehere.close()
      setalarm()

def setalarm():
    extractedTime = open("Alarmtext.txt","rt")
    time = extractedTime.read()
    Time = str(time)
    extractedTime.close()

    deleteTime = open("Alarmtext.txt","r+")
    deleteTime.truncate(0)
    deleteTime.close()
    ring(Time)


def ring(Time):
    timeSet = Time
    timeNow = timeSet.replace(ASSISTANT_NAME,"")
    timeNow = timeSet.replace("set an alarm","")
    timeNow = timeSet.replace(" and ",":") 
    alarmTime = str(timeNow)
    print("Alarm is set for:- "+ alarmTime)
    speak("Done sir")
    closeCheck = alarmCloseCheck(alarmTime)
    while True:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        if currentTime == alarmTime:
            speak("Alarm ringing, sir")
            musicLoc = "www\\assets\\Audio\\01-Theher-Ja-Bestsongs.pk.mp3"
            playsound(musicLoc)
        elif currentTime == closeCheck:
            exit()

def alarmCloseCheck(time):
    time_str1 = time
    time_str2 = "00:00:25"

    time_delta1 = datetime.datetime.strptime(time_str1, "%H:%M:%S")
    time_delta2 = datetime.datetime.strptime(time_str2, "%H:%M:%S")

    # Perform addition
    result_time = time_delta1 + (time_delta2 - datetime.datetime(1900, 1, 1))

    # Format the result back into the desired time format
    result_time_str = str(result_time.strftime("%H:%M:%S"))

    return  result_time_str


#  REMEMBER Function

def rememberFunction(query):
    rememberMessage = query.replace("remember that","")
    rememberMessage = query.replace("remembered that","")
    rememberMessage = query.replace(ASSISTANT_NAME,"")
    speak("You told me "+rememberMessage)
    remember = open("Remember.txt","a")
    remember.write(rememberMessage)
    remember.close()

def rememberCheck():
    remember = open("Remember.txt","r")
    if not remember.read():
        speak("You told me nothing")
        remember.close()
    else:
        remember = open("Remember.txt", "r")
        speak("You told me " + remember.read())
        remember.close()
        delete = open("Remember.txt","r+")
        delete.truncate(0)
        delete.close()


#   YOUTUBE
        
keyboard = Controller()

def volumeUp():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumeDown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)

def playNext():
    pyautogui.hotkey("Shift", "n")

def playPrevious():
    pyautogui.hotkey("Shift", "p")
    
def moveFB(query):
    for i in range(2):
        if "forward" in query:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif "backward" in query:
            keyboard.press(Key.left)
            keyboard.release(Key.left)

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None
