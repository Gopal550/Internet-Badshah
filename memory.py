import json
import os

FILE = "yaad.json"

def yaad_dalo(line):
    data = sab_yaad()
    if line not in data:
        data.append(line)
        with open(FILE, "w") as f:
            json.dump(data, f)

def sab_yaad():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []
    import json
import os

FILE = "yaad.json"

def yaad_dalo(line):
    data = sab_yaad()
    if line not in data:
        data.append(line)
        with open(FILE, "w") as f:
            json.dump(data, f)

def sab_yaad():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []