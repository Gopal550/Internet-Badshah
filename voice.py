import speech_recognition as sr
from gtts import gTTS
import os

def bolo(text):
    print("Badshah:", text)
    tts = gTTS(text=text, lang="hi")
    tts.save("badshah.mp3")
    os.system("mpg123 badshah.mp3")  # Yeh line playsound ka replacement hai
    os.remove("badshah.mp3")

def suno():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Badshah sun raha hai...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="hi-IN").lower()
    except:
        bolo("Kuch samajh nahi aaya.")
        return ""
        @app.route("/owner_voice.wav")
def play_voice():
    return send_file("owner_voice.wav")