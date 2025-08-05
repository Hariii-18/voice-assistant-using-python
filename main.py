import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

# this part of code will recognise what we speak 
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing..")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Sorry, i could not match you , say again")

# this part of code will speak 
def spechtx(x):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)  #[0] = male voice , [1] = female voice

    rate = engine.getProperty("rate")
    engine.setProperty("rate" , 170)  #setting the voice speed of assistant
    
    engine.say(x)
    engine.runAndWait()


# 
if __name__ == '__main__' :

    if sptext().lower() == "hey jarvis":
        print('Hello User , How can i help you..')
    else:
        print("sorry , i did'nt get you ")
        