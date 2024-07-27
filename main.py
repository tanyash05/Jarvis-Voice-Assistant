import pyttsx3
import speech_recognition 
import datetime
import pyautogui
import os
import speedtest
from translate import translategl

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding.....")
        query  = r.recognize_google(audio,language='en-in')
        print(f"==> Me : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from greet import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "bye" in query:
                    speak("Ok,You can me call anytime")
                    break

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "translate" in query:
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "hello" in query:
                    speak("Hello, how are you ?")
                elif "i am fine" in query:
                    speak("that's great!")
                elif "how are you" in query:
                    speak("I'm Perfect!")
                elif "thank you" in query:
                    speak("you are welcome!")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("turning volume up!")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("turning volume down!")
                    volumedown()

                

                elif "open" in query:
                    from dict import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dict import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from news import latestnews
                    latestnews()
                
                elif "calculate" in query:
                    from calculator import WolfRamAlpha
                    from calculator import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from whatsapp import sendMessage
                    sendMessage()

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"the time is {strTime}")

                elif "see you next time" in query:
                    speak("Shutting down!")
                    exit()