import speech_recognition as sr
import pyaudio
import pywhatkit

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source) 
        print("Say something...")
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    return text

text = get_audio()

if "youtube" in text.lower():
    pywhatkit.playonyt(text)
else:
    pywhatkit.search(text)