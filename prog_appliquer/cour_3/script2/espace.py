# espace.py
# Note: il nous faut installer 'pip install requests' 
import requests
import json  #pour loads()

# donnée json sous la forme d'une chaîne
employe= '{"prénom": "Viktor", "nom": "Korchnoi", "département": "Informatique"}'

print(type(employe)) # <class 'str'>

# convertir la chaîne vers un objet json
objet_json = json.loads(employe)

print(type(objet_json)) # <class 'dict'>

print(objet_json["nom"])  # Korchnoi

astronautes = requests.get('http://api.open-notify.org/astros.json')
print(astronautes)
# <Response [200]>
print(type(astronautes)) # <class 'requests.models.Response'>
json_astronautes  = astronautes.json()
print(json_astronautes)
#{'number': 10, 'people': [{'name': 'Sergey Prokopyev', 'craft': 'ISS'},
#                         {'name': 'Dmitry Petelin', 'craft': 'ISS'},
#                          {'name': 'Frank Rubio', 'craft': 'ISS'},
#                          {'name': 'Stephen Bowen', 'craft': 'ISS'},
#                          {'name': 'Warren Hoburg', 'craft': 'ISS'},
#                          {'name': 'Sultan Alneyadi', 'craft': 'ISS'},
#                          {'name': 'Andrey Fedyaev', 'craft': 'ISS'},
#                          {'name': 'Jing Haiping', 'craft': 'Tiangong'},
#                          {'name': 'Gui Haichow', 'craft': 'Tiangong'},
#                          {'name': 'Zhu Yangzhu', 'craft': 'Tiangong'}],
# 'message': 'success'}

print("Les gens dans l'espace:")
for p in json_astronautes['people']:
    print(p['name'])
# Sergey Prokopyev Dmitry Petelin Frank Rubio Stephen Bowen Warren Hoburg Sultan Alneyadi
# Andrey Fedyaev Jing Haiping Gui Haichow Zhu Yangzhu




