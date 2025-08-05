import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime
import pyjokes
import os
import random


# this part of code will recognise what we speak 
def input():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing..")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}") #displays recognized speech 
            return data
        except sr.UnknownValueError:
            print("Sorry, i could not match you , say again")
            return ""

# this part of code will speak 
def speak(x):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)  #[0] = male voice , [1] = female voice

    rate = engine.getProperty("rate")
    engine.setProperty("rate" , 200)  #setting the voice speed of assistant

    print("Assistant says:", x)      #  Print the same text being spoken
    engine.say(x)
    engine.runAndWait()
   


# the commands for assistant

if __name__ == '__main__' :
    
    while True:
        data1 = input().lower()
        if not data1:
            continue
        if "your name" in data1 :
            name = "my name is jarvis , your personal assistant"
            speak(name)

        elif "hey jarvis" in data1 :
            reply = "Hello User , How can i help you"
            speak(reply)
        
        elif "old are you" in data1:
            age = "im one year old"
            speak(age)
        
        elif any(phrase in data1 for phrase in ["what is the time", "now time", "date and time", "today date"]):
            current_time = datetime.now().strftime("%I:%M%p")
            speak(current_time)

        elif any(phrase in data1 for phrase in ["open youtube", "youtube", "hey jarvis open youtube"]): #if user speak any one out of these sentences assistant can easily get what we say
            webbrowser.open("https://www.youtube.com/")

        elif any(phrase in data1 for phrase in ["google", "open google", "hey jarvis open google"]):
            webbrowser.open("https://www.google.com/")

        elif any(phrase in data1 for phrase in ["github", "open github", "hey jarvis open github"]):
            webbrowser.open("https://github.com/")
        
        elif any(pharse in data1 for pharse in["joke","tell me a joke","tell joke","hey jarvis tell me a joke"]):
            joke = pyjokes.get_joke(language="en")
            speak(joke)
        
        elif any(phrase in data1 for phrase in ["open documents", "open my documents", "open my pc documents"]):
            address = r"C:\Users\hari\OneDrive\Documents"
            os.startfile(address)
            
        elif any(phrase in data1 for phrase in ["play telugu songs", "play songs on youtube", "play telugu songs on youtube"]):
            songs ="https://www.youtube.com/watch?v=VQ2-HPwxAZY&list=RDQMg5xeA07Wevs&start_radio=1"
            webbrowser.open(songs)

        elif any(phrase in data1 for phrase in ["thank you jarvis", "thank you", "bye" ,"exit","ok bye"]):
            farewells = [
                        "You're welcome! Have a great day!",
                        "Anytime, boss! Jarvis signing off.",
                        "See you soon! Take care!",
                        "Logging off... but I'll be right here when you need me again!",
                        "Session terminated. Awaiting next command!"
                    ]
            speak(random.choice(farewells))

        break
else:
    print("sorry , i did'nt get you ")