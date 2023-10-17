import json

with open("body.json", mode="r", encoding="utf-8") as data:
    body = json.load(data)

hodnoceni = {}

for jmeno, ziskane_body in body.items():
    if body[jmeno] >= 60:
        hodnoceni[jmeno] = "Pass"
    else:
        hodnoceni[jmeno] = "Fail"


with open("prospech.json", mode="w", encoding="utf-8") as ukol:
    json.dump(hodnoceni, ukol, ensure_ascii=False)
    