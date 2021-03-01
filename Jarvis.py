import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install pustil
import pyjokes #pip install pyjokes
import random
import operator
import json
import wolframalpha
import time
import winshell
from urllib.request import urlopen
import requests
import winshell

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def time_():
    #Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak("the current time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak(Time)

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Shreyansh!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis 1 point O at your service. Please tell me how can I help you?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('swaggyhell.master@gmail.com', 'sagr22042514')
    server.sendmail('swaggyhell.master@gmail.com', to, content)
    server.close()
#     speak("Email has been sent.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/CWC/Desktop/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(str(battery.percent)+"percent")

def jokes():
    joke =pyjokes.get_joke() 
#     print(joke)
    speak(joke)

def Introduction():
    speak("I am JARVIS 1.0 , Personal AI assistant , "
    "I am created by Shreyansh , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")
    
def Creator():
    speak("Shreyansh is an extra-ordinary person , He loves to be lazy, "
    "He is very co-operative and has been very careful while developing me,"
    "If you are facing any problem regarding the 'Jarvis', He will be glad to help you ")


if __name__ == '__main__':


    clear = lambda: os.system('cls') 
    # This Function will clean any 
    # command before execution of this python file
    clear()

    wishme()
    
    while True:
        query = TakeCommand().lower()
        # All the commands said by user will be 
        # stored here in 'query' and will be 
        # converted to lower case for easily 
        # recognition of command 
        if 'jarvis' in query:
            line = query.split()
            line.remove('jarvis')
            query = " ".join(line)
            
        if 'hi' in query or 'hello' in query or 'hey' in query:
            speak('Hello sir.')
            
        elif 'how are you' in query:
            speak("I am fine, Sir Thanks for asking")
            speak("How are you Sir?")
            query = TakeCommand().lower()
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")
                
        elif 'time' in query:
            time_()
            
        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
#             print(result)
            speak(result)
        
        elif 'open youtube' in query or 'search in youtube' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)
            
        elif 'search google' in query or 'open google' in query:
            speak("What should I search?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        
        #elif 'search' in query: 
            #query = query.replace("query","")
            #wb.open(query)
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
            
        elif "why you came to this world" in query:
            speak("Thanks to Shreyansh. Further it is a secret")
            
        elif 'ms word' in query:
            speak("opening MS Word")
            word = r'C:\Users\CWC\AppData\Local\Microsoft\WindowsApps\Microsoft.Office.Desktop_8wekyb3d8bbwe\winword.exe'
            os.startfile(word)

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'empty recycle bin' in query or 'dump everything in recycle bin' in query or 'recycle bin' in query:
            try:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled") 
                print("Done")
            except:
                speak('Recycle bin is already empty')
                
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
                
        elif 'search in chrome' in query or 'open chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
        
        elif 'log out' in query:
            os.system("shutdown -l")
            
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            
        elif 'play songs' in query or 'entertain me' in query or 'song' in query or 'songs' in query:
            video ='F:/iiitp/work/self/Videos'
            audio ='F:/phone data/ngp phone data/songs ngp'
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            if 'audio' not in ans or 'video' not in ans:
                flag_song=1
                while(flag_song==1):
                    speak("I could not understand you. Please Try again.")
                    ans = (TakeCommand().lower())
                    if 'audio' in ans or 'video' in ans:
                        flag_song=0
                
            elif 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            #used while loop to keep the jarvis on the speak command untill req. command is given.
            while('number' not in rand and rand != 'random'):                       
                #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and 
                #then checked if it is according to reuirement or not. And if it is not which means while loop is true, 
                #then commands under 'while loop' will execute untill desired approach.
                #As it will again ask the user for input in the same block. 
                
                speak("I could not understand you. Please Try again.")          
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            elif 'random' in rand or 'randomly' in rand:
                    rand = random.randint(1,6)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
                

        elif 'remember that' in query or 'remember' in query or 'remind me' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query or 'memory' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query or 'show me notes' in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 
        
        #General Questions
        elif "what is" in query or "who is" in query: 
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client("9K4RGY-67J8VL6PYG")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 

        #show location on map
        elif "where is" in query or 'locate' in query or 'map' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        elif "weather" in query: 
            # Google Open weather website 
            # to get API of Open weather
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

            # City Name 
            speak("City name")
            city = TakeCommand()
            print("City name:",city)
            # API key 
            API_KEY = "0c42f7f6b53b244c78a418f4f181282a"
            # upadting the URL
            URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
            # print(URL)
            # HTTP request
            response = requests.get(URL)
            # checking the status code of the request
            if response.status_code == 200:
                # getting data in the json format
                data = response.json()
                # getting the main dict block
                main = data['main']
                # getting temperature
                temperature = main['temp']
                # getting the humidity
                humidity = main['humidity']
                # getting the pressure
                pressure = main['pressure']
                # weather report
                report = data['weather']
                print(f"{city:-^30}")
#                 print(f"Temperature(in K): {temperature}")
                speak("the temperature right now at"+city+"is"+str(temperature))
#                 print(f"Humidity: {humidity}")
                speak("humidity is"+str(humidity))
#                 print(f"Pressure: {pressure}")
                speak("air pressure is"+str(pressure))
#                 print(f"Weather Report: {report[0]['description']}")
                speak("the report in the city overall says it is" + report[0]['description'])
            else:
               # showing the error message
                speak("Error in the HTTP request") 
        
        elif 'news' in query or 'headlines' in query:
            try:
                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=6096b072c578419a879f5af7e26297b1')
                data = json.load(jsonObj)
                i = 1 
                speak('here are some top entertainment news from india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    if item['description']:
                        print(item['description'] + '\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e)) 

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")  
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
            
        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()
            
        elif 'tell me about shreyansh' and 'creator' in query:
            Creator()
        
        
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        
        #calculation
        elif "calculate" in query:
            app_id = "9K4RGY-67J8VL6PYG"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        
        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query or 'quit' in query or 'good bye' in query or 'bye' in query or 'goodnight' in query:
            speak('I hope you liked my service sir. See you soon.')
            speak("going Offline")
            break
