import speech_recognition as sr


def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source) 
        print("Say something...")
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
    return text

get_audio()