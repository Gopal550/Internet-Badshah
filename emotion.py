# engine/emotion.py

def mood_pehchano(hukum):
    hukum = hukum.lower()
    if any(word in hukum for word in ["gussa", "naraz", "chod", "pagal"]):
        return "gussa"
    elif any(word in hukum for word in ["pyaar", "yaar", "bhai", "dil"]):
        return "pyaar"
    elif any(word in hukum for word in ["majak", "has", "joke"]):
        return "majak"
    elif any(word in hukum for word in ["dukhi", "udaas", "ro"]):
        return "gham"
    else:
        return "neutral"

def emotion_ke_sath(text, mood):
    if mood == "gussa":
        return f"Thik hai Badshah! {text.upper()}!!"
    elif mood == "pyaar":
        return f"Pyaar bhara jawab: {text}"
    elif mood == "majak":
        return f"Ek chutkula sunte sunte: {text}"
    elif mood == "gham":
        return f"Main samajh sakta hoon Badshah... {text}"
    else:
        return text