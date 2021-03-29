import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import pyttsx3
import pyaudio

r = sr.Recognizer()
r.energy_threshold = 4000
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    my_text = r.recognize_google(audio)

    if my_text == "hi how are you":
        speech = gTTS(text = "I am fine! How about you?")
        speech.save('audio.mp3')
        playsound('audio.mp3')
        os.remove('audio.mp3')

    elif my_text == "open game":
        speech = gTTS(text = "opening game launcher")
        speech.save('audio.mp3')
        playsound('audio.mp3')
        os.remove('audio.mp3')
        os.startfile("C:\Program Files (x86)\Steam\steam.exe")

    elif my_text == "close":
        speech = gTTS(text = "shut the fuck up MOTHERFUCKER")
        speech.save("audio.mp3")
        playsound("audio.mp3")
        os.remove("audio.mp3")

    elif my_text == "open chrome" or "open browser":
        speech = gTTS(text = "opening google chrome")
        speech.save("audio.mp3")
        playsound("audio.mp3")
        os.remove("audio.mp3")
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

    else:
        exit(0)