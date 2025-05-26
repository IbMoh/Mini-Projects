import json
FILE = 'Home.json'

d = {"light":"off","door":"open"}

"""
json_d = json.dumps(d, indent=3)

with open(FILE,'r+') as w:
    w.write(json_d)
"""

inp = input("> ")

li = inp.split()


with open(FILE) as f:
    DATA = json.load(f)
    f.close()

for key,value in DATA.items():
    if key == li[0]:
        DATA[key] = li[1]

print(DATA)
print(li[0])
