import pyttsx3
import speech_recognition as sr
import datetime
import os
import time
import cv2
import random
import pywhatkit as kit
import operator
import sys
from requests import get
from bs4 import BeautifulSoup
import requests as res
from pynput import keyboard
import requests
from self import self
import function as fn
import webbrowser
import decouple
import smtplib
import pyjokes
import psutil
import wikipedia
import instaloader
import pyautogui




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}")
        
    except Exception as e:
        #speak("Say that again please...")
        return "none"
    query = query.lower()
    return query
     
 

    
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%p")
    
    if hour>=0 and hour<=12:
        speak(f"Good morning Sir!, its {tt}")
        
    elif hour>12 and hour<18:
        speak(f"Good afternoon Sir!, its {tt}")
        
    else:
        speak(f"Good evening Sir!, its {tt}")
        
    speak("Im SANTA . please tell me sir how can I help you ?")
    

def sendEmail(to, content):
    server = smtplib.SMTP ('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to,content)
    server.close()
    
    
def TaskExecution():
    wish()
    while True:
    #if 1:
        
        query = takecommand().lower()
        
        
        if 'open notepad' in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
            while True:
                notepadQuery = takecommand().lower()
                if 'paste' in notepadQuery:
                    pyautogui.hotkey('ctrl','v')
                    speak("Done sir !")
                    
                elif 'save this file' in notepadQuery:
                    pyautogui.hotkey('ctrl', 's')
                    speak("sir, please Specify a name for this file")
                    notepadSavingQuery = takecommand()
                    pyautogui.write(notepadSavingQuery)
                    pyautogui.press("enter")
                    
                elif 'type' in notepadQuery:
                    speak("please tell me what should i write...")
                    
                    while True:
                        writeInNotepad = takecommand()
                        if writeInNotepad == 'exit typing':
                            speak("Done sir")
                            break
                        else:
                            pyautogui.write(writeInNotepad)
                    
                elif 'exit notepad' in notepadQuery or 'close notepad' in notepadQuery:
                    speak("quiting notepad sir...")
                    pyautogui.hotkey('ctrl','w')
                    break
            
        elif 'open command prompt' in query:
            os.system("start cmd")
        
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            
        elif 'open windows' in query:
            speak("opening window")
            pyautogui.hotkey('win')
            
        elif 'open my computer' in query:
            speak("opening files")
            pyautogui.hotkey('win','e')
            
        elif 'open settings' in query:
            pyautogui.hotkey('win','i')
            
        elif 'play a movie' in query:
            vid_dir = "D:\\Dhanush\\movies"
            video = os.listdir(vid_dir)
            rd = random.choice(video)
            os.startfile(os.path.join(vid_dir, rd))
            
            
        elif 'play music' in query:
            music_dir = "C://Users//91978//Music//XXX-TENTACION"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif 'internet speed' in query:
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")
                
            
        elif 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak(f"{results}")
            print(results)
            
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            
        elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")
            
        elif 'open stackoverflow' in query:
                webbrowser.open("www.stackoverflow.com")
                
        elif 'open google' in query:
            speak("Sir, what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            
        elif 'send message' in query:
            kit.sendwhatmsg("+918344505279", "This is testing protocol",2,25)
            
        elif 'play songs on youtube' in query:
            kit.playonyt("XXXTENTACION Changes")
            
        elif 'email to Light' in query:
            try:
                speak("What should I say ?")
                content = takecommand().lower()
                to = "dhanuskd64@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent to Light")
                
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this mail ")
                
        elif 'no thanks' in query:
            speak("Thanks for using me Sir! , have a great day sir")
            break
            
        elif 'close notepad' in query:
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif 'close command prompt' in query:
            speak("closing command prompt")
            os.system("taskkill /f /im cmd.exe")
            
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "C://Users//91978//Music//XXX-TENTACION"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
                
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
                
        elif 'tell me a joke' in query:
            joke = pyjokes.get_jokes()
            speak(joke)
            
        elif 'Where I am' in query:
            speak("One minute sir! , Let me check")
          
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/+'ipAdd'+.json"
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"Sir I am  not sure, but I think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry Sir , Due to network issue I am not able to find where we are.")
                pass
            
        elif 'profile on instagram' in query:
            speak("Sir please enter the user name correctly.")
            name = input("Enter user name here:")
            webbrowser.open(f"www.instagram.com/{name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done sir , profile picture saved in our main folder. now I am ready for next command")
            else:
                pass
                
        elif 'tempreture' in query:
            search = "tempreture in Tamilnadu"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
            
        elif 'take a screenshot' in query:
            speak("Sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few seconds, I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is saved in our main folder. now I am ready for next command")
            
        elif 'minimize' in query or 'minimise' in query:
            speak("minimizing this window sir")
            pyautogui.hotkey('win','down','down')
            
        elif 'maximize' in query or 'maximise' in query:
             speak("maximizing this window sir")
             pyautogui.hotkey('win','up','up')
             
        elif 'close the window' in query or 'close the application' in query:
            speak("closing the window sir")
            pyautogui.hotkey('ctrl','w')
            
        elif 'lock screen' in query:
            speak("ok sir!, locking the screen")
            pyautogui.hotkey('win', 'l')
            
        elif 'show notification' in query:
            speak("ok sir")
            pyautogui.hotkey('win','n')
            
        elif 'open accessibility' in query:
            speak("opening accessibility")
            pyautogui.hotkey('win', 'u')
            
        elif 'increase volume' in query:
            speak("increasing sir")
            pyautogui.press('volumeup')
            
        elif 'decrease volume' in query:
            speak("decreasing sir")
            pyautogui.press('volumedown')
            
        elif 'mute volume' in query:
            speak("ok sir")
            pyautogui.press('volumemute')
            
        elif "how much power left" in query or "battery power" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir we have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            
            elif percentage>=40 and percentage>=70:
                speak("we should connect our system to charging point to charge our battery")
                
            elif percentage<=15 and percentage<=30:
                speak("very low power sir , we have to plugin the charge")
                
            elif percentage<=15:
                speak("no power left sir please charge ,the system gonna shutdown")
                break
            
        elif 'open task manager' in query:
            speak("opening task manager")
            pyautogui.hotkey('ctrl','shift','esc')
            
        elif 'action center' in query:
            speak("opening")
            pyautogui.hotkey('win', 'a')
            
        elif 'show hidden icons' in query:
            speak("showing hidden icons")
            pyautogui.hotkey('win','b','enter')
           
        elif 'project settings' in query:
            speak("opening")
            pyautogui.hotkey('win', 'p')
            
        elif 'screen clipping' in query:
            speak("clipping sir!")
            pyautogui.hotkey('win', 'shift', 's')
            
        elif 'launch emoji' in query:
            speak("launching keyboard")
            pyautogui.hotkey('win','.')
            
        elif 'open voice typing' in query:
            speak("opening")
            pyautogui.hotkey('win','h')
            
        elif 'open game options' in query:
            speak("opening game options")
            pyautogui.hotkey('win', 'g')
        
        elif 'shutdown system' in query:
            os.system("shutdown /s /t 5")
            
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
            
        elif 'sleep the system' in query:
            os.system("rund1132.exe powerprof.d11,SetSuspendState 0,1,0")
            
        elif 'who are you' in query:
            speak("I am SANTA, Im a basic version of AI and I was devoloped by the Boys gang")
            
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takecommand().lower()
            kit(number, message)
            speak("I've sent the message sir.")
            
        elif 'hide this file' in query or 'hide this folder' in query or 'visible everyone' in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if 'hide' in condition:
                    os.system("attrib +h /s /d")
                    speak("sir all the files in this folder are hidden now")
                
            elif 'visible' in condition:
                    os.system("attrib -h /s /d")
                    speak("sir all the files in this folder are visible now for everyone")
                
            elif 'leave it' or 'leave for now' in condition:
                    speak("ok sir!")
                    break           
                
        elif 'hello' in query or 'hey' in query:
             speak("hello sir , may I help you with something.")
             
        elif 'how are you' in query:
             speak("i am fine sir , what about you ?")
             
        elif 'also good' in query:
             speak("thats great to hear from you.")
             
        elif 'can you calculate this' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate,example:60 plus 4")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+': operator.add, 
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                    }[op]
            def eval_binary_expr(op1, oper,op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            
             
        elif 'thank you' in query or 'thanks' in query:
             speak("Its my pleasure sir!")
               
             
        elif 'you can sleep now' in query:
             speak("Ok sir")
             break
                
            
if __name__=="__main__":
    
    while True:
        
        permission = takecommand()
        
        if 'santa' in permission or 'start santa' in permission:
            TaskExecution()
            
        elif 'goodbye' in permission or 'shut up' in permission:
            speak("Thanks for using me Sir! , have a great day sir")
            sys.exit()
            
        elif 'exit you' in permission:
            speak("ok sir ,Thanks for using me !")
            sys.exit()

            speak("Sir do you have any other work sir ?")
            
            if 'no' in permission:
                speak("sir can i sleep now")
                
               