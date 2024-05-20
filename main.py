import speech_recognition as sr
import pyaudio
import pywhatkit
import pyautogui
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
elif "info" in text.lower():
    try:
        print("Attempting to fetch info...")
        info = pywhatkit.info(text, lines=5)
        print("Info fetched successfully.")
        print(info)
        speech(info)
    except Exception as e:
        print(f"An error occurred: {e}")
        speech("Sorry, I couldn't fetch the information.")
elif "screenshot" in text.lower():
      # Take a screenshot
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("myscreenshot.png")
        speech("Screenshot taken and saved as myscreenshot.png")
    except Exception as e:
        print(f"An error occurred: {e}")
        speech("Sorry, I couldn't take the screenshot.")
elif "joke" in text.lower():
    speech("What does a storm cloud wear under his raincoat? Thunderwear.")
else:
    speech("Okay, i will find it on browser")
    pywhatkit.search(text)