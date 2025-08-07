# voice-assistant-using-python
A Python-based personal voice assistant that responds to voice commands to perform everyday tasks like opening apps, fetching info, and web browsing. Combines speech recognition, text-to-speech, and smart logic for hands-free interaction.

# 🧠 Jarvis - Voice Controlled Desktop Assistant

A simple yet functional voice-controlled desktop assistant built with Python. This assistant, named **Jarvis**, can understand your voice commands, speak responses, open websites, tell jokes, and perform basic tasks like opening folders or telling the time.

---

## 📌 Features

- 🎙️ **Voice Recognition** using Google Speech Recognition
- 🗣️ **Text-to-Speech Output** using `pyttsx3`
- 🕒 Tells you the current **time and date**
- 🌐 Opens popular websites like **YouTube**, **Google**, and **GitHub**
- 🎵 Plays **Telugu songs** on YouTube
- 📂 Opens **Documents** folder on your system
- 🤖 Tells funny **jokes** with the `pyjokes` library
- 💬 Friendly interaction with pre-defined responses

---

## 🛠️ Technologies Used

- `pyttsx3` – Text-to-speech conversion
- `speech_recognition` – For recognizing voice input
- `webbrowser` – To open URLs
- `datetime` – To fetch current time
- `pyjokes` – To generate jokes
- `os` – To access local file system
- `random` – To pick random responses

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/jarvis-assistant.git
   cd jarvis-assistant

2.Install required libraries
    pip install pyttsx3 SpeechRecognition pyjokes

3. Run the assistant
    python jarvis.py


USAGE: 
Once the script is running:

Speak clearly after the “Listening…” prompt appears.

-Try saying:

Hey Jarvis

What is the time?

Open YouTube

Tell me a joke

Open Documents

Play Telugu songs

Thank you Jarvis

To exit, say:

Bye, Exit, or Thank you


🔒 Note
Make sure your microphone is properly connected and working.



📁 Folder Structure

jarvis-assistant/
│
├── jarvis.py            # Main program file
├── README.md            # Project description
└── requirements.txt     # Optional: List of dependencies


🙋‍♂️ Author
Hari Prasad
Inspired by J.A.R.V.I.S. from Marvel. Built for learning purposes.