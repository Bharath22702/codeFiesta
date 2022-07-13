import json
from googletrans import Translator
translator = Translator()
file = 'text.txt'
dict = {}

with open(file) as fn:
    for d in fn:
        try:
            key, desc = d.strip().split(None, 1)
            dict[key] = desc.strip()
        except:pass

otfile = open("output.json", "w")
json.dump(dict, otfile)
otfile.close()

