import webbrowser

def internet_ka_control(hukum):
    if "youtube" in hukum:
        webbrowser.open("https://www.youtube.com")
        return "YouTube kholo raha hoon."
    elif "google" in hukum:
        webbrowser.open("https://www.google.com")
        return "Google kholo raha hoon."
    elif "facebook" in hukum:
        webbrowser.open("https://www.facebook.com")
        return "Facebook kholo raha hoon."
    elif "open" in hukum:
        words = hukum.split("open")[-1].strip()
        url = f"https://{words.replace(' ', '')}.com"
        webbrowser.open(url)
        return f"{url} kholo raha hoon."
    else:
        return ""
        import webbrowser
import requests

def khol(command):
    if "google" in command:
        query = command.replace("google", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Google par dhoondha: {query}"
    elif "youtube" in command:
        query = command.replace("youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"YouTube par dhoondha: {query}"
    elif "news" in command:
        webbrowser.open("https://news.google.com")
        return "Yeh lo, Google News"
    elif "instagram" in command:
        webbrowser.open("https://www.instagram.com")
        return "Instagram khol diya"
    elif "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather")
        return "Weather bata raha hoon"
    else:
        return "Kya kholna hai, yeh samajh nahi aaya."
        # engine/internet.py

import webbrowser

def browser_khol(site):
    try:
        if "http" not in site:
            site = "https://www." + site + ".com"
        webbrowser.open(site)
        return f"{site} khol diya gaya hai, Badshah."
    except:
        return "Site kholne mein dikkat aayi, Badshah."