# Internet Badshah v∞ — Engine Initialization
# Yeh file sabhi tapes (voice, brain, control, memory, API, internet) ko integrate karti hai

from .voice import suno, bolo
from .brain import soch
from .control import samrajya
from .memory import yaad_dalo, sab_yaad
from .api import api_khol
from .internet import browser_khol

def start_badshah():
    bolo("Badshah samrajya mein pravesh kar chuka hai.")
    while True:
        hukum = suno()
        if not hukum:
            continue

        if "band ho ja" in hukum or "bye" in hukum:
            bolo("Badshah chhup ho raha hai. Jay Hind.")
            break

        elif "yaad kya hai" in hukum:
            sab = sab_yaad()
            if sab:
                bolo("Main yeh sab yaad rakha hoon:")
                for i in sab:
                    bolo(i)
            else:
                bolo("Abhi kuch yaad nahi Badshah.")

        elif "open api" in hukum or "api" in hukum:
            bolo("API control khol raha hoon...")
            api_khol()

        elif "internet" in hukum or "browser" in hukum:
            bolo("Internet browser chalu kar raha hoon...")
            browser_khol()

        else:
            yaad_dalo(hukum)
            jawab = soch(hukum)
            bolo(jawab)
            from engine import start_badshah

if __name__ == "__main__":
    start_badshah()