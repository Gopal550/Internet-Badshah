# engine/api.py

def get_weather(sheher):
    return f"{sheher.title()} ka mausam aaj shaant hai, Badshah."

def search_google(query):
    return f"Google par yeh dhoondh raha hoon: '{query}'"

def api_khol(app_naam):
    app_naam = app_naam.lower()
    
    if "instagram" in app_naam:
        return "Instagram khol raha hoon..."
    elif "youtube" in app_naam:
        return "YouTube chalu kar raha hoon..."
    elif "google" in app_naam:
        return "Google pr ja raha hoon..."
    elif "chatgpt" in app_naam:
        return "ChatGPT pr connection bana raha hoon..."
    else:
        return "Konsi app kholni hai Badshah?"