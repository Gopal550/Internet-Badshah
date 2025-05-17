
import sounddevice as sd
import numpy as np
import os

SAVED_FILE = "voiceprint.npy"

def record_voice(duration=2, fs=44100):
    print("Awaaz sun raha hoon...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return np.array(audio).flatten()

def register_voice():
    voice_data = record_voice()
    np.save(SAVED_FILE, voice_data)
    import os

def match_voice():
    print("Matching voice in TESTING MODE...")
    return os.path.exists("owner_voice.wav")

def match_voice():
    if not os.path.exists(SAVED_FILE):
        return False
    saved = np.load(SAVED_FILE)
    current = record_voice()
    similarity = np.corrcoef(saved, current)[0][1]
    return similarity > 0.85