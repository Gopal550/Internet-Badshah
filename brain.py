from engine.internet import internet_ka_control
from engine.api import get_weather, search_google

def soch(hukum):
    hukum = hukum.lower()

    # Internet control
    internet_jawab = internet_ka_control(hukum)
    if internet_jawab:
        return internet_jawab

    # Identity & capability
    if "kaun hai tu" in hukum or "tum kaun ho" in hukum:
        return "Main Badshah hoon — sirf Gopal ke liye, duniya ke liye nahi."

    elif "tum kya kar sakte ho" in hukum:
        return "Main internet, apps, automation, memory, learning, aur duniya ko control kar sakta hoon. Aap hukum do."

    # Specific app triggers
    elif "internet chalu karo" in hukum:
        return "Internet ki taaqat activate kar raha hoon Badshah."

    elif "instagram khol" in hukum:
        return "Instagram khol raha hoon..."

    elif "youtube chalu karo" in hukum:
        return "YouTube chalu kar raha hoon..."

    elif "google pe jao" in hukum:
        return "Google pr ja raha hoon..."

    elif "chatgpt chalu karo" in hukum:
        return "ChatGPT pr connection bana raha hoon..."

    # Weather access
    elif "mausam" in hukum or "weather" in hukum:
        sheher = hukum.split("mausam")[-1].strip()
        if not sheher:
            return "Badshah, kis sheher ka mausam dekhna hai?"
        return get_weather(sheher)

    # Google search
    elif "google" in hukum:
        query = hukum.replace("google", "").strip()
        if query:
            return search_google(query)
        return "Kya khojna hai Badshah?"

    # Default memory response
    else:
        return f"Tumne kaha: {hukum}. Main ise yaad rakhunga aur sudharunga."