import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source) 
        print("Say something...")
        playsound("./sounds/piano.mp3")
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    return text

text = get_audio()

if "youtube" in text.lower():
    speech(f"Okay, i will bring {text} for you")
    pywhatkit.playonyt(text)
elif "joke" in text.lower():
    speech("What does a storm cloud wear under his raincoat? Thunderwear.")
else:
    speech("Okay, i will find it on browser")
    pywhatkit.search(text)