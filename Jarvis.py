import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init()

# speaking through the computer's internal command engine
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
# speak("Hello Shreyansh Gupta")

# checking the background timestamp of the area you are in.
def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S") # for 24 hour clock use %H in place of %H
    speak("The current time is")
    speak(Time)
# time_()

# configuring date of the administrative system
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("Current date is")
    speak(date)
    speak(month)
    speak(year)   
# date_()

# configuring wishing the administrator service on
def wishme():
    speak("Welcome back Shreyansh")
    date_()
    time_()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<16:
        speak("Good afternoon sir!")
    elif hour>=16 and hour<19:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("Jarvis 1 point O at your service! What would you like me to do?")
# wishme()

# taking input command from the user.
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please....")
        return None
    return query
# TakeCommand()

if __name__ == "__main__":
    # bringing things in action
    wishme()
    
    while True:
        query = TakeCommand().lower()
        #all commands in lower case for easy recognition
        
        if "time" in query:
            time_()
            
        elif "date" in query:
            date_()
        
        elif "wikipedia" in query or "search" in query:
            speak("Searching.....")
            query = query.replace("wikipedia","")
            try:
                result = wikipedia.summary(query,sentences = 3)
                speak('According to wikipedia')
                print(result)
                speak(result)
            except:
                speak("I'm sorry sir. There was nothing i found about the search on Wikipedia.")
            string1 = result
        elif "system command help" in query:
            speak("System command launching..")
            print("System command launching..")
            speak("Jarvis 1.0 at your service right now can tell you about timestamps and can fetch details for you from Wikipedia.")
            print("Jarvis 1.0 at your service right now can tell you about timestamps and can fetch details for you from Wikipedia.")
        elif "please repeat" in query:
            speak(string1)
            print(string1)
        elif 'thank you' in query:
            speak('Welcome sir! Would you like me to do anything else?')
            command = TakeCommand().lower()
            if "yes" in command:
                pass
            elif "no" in command:
                break
        elif 'quit' in query:
            break
        
        
#         try: 
#             from googlesearch import search 
#         except ImportError:  
#             print("No module named 'google' found") 

#         # to search 
#         query = "A computer science portal"

#         for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
#             print(j)
            
#         from googlesearch import search
#         search("Google", lang="fr")
