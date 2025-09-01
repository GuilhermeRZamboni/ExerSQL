import requests

b = requests.get("https://www.curseforge.com/api/v1/mods/687131/files")
a = b.json()
