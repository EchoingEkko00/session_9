# temperature.py
# Note: il nous faut installer 'pip install requests' 
import requests
# Inscrivez-vous à http://api.openweathermap.org pour obtenir une clé pour utiliser l'API
api_cle = 'd5a8b5763b8ab92ff4d803faf6b212ff' # la mienne
ville = 'Montreal'
url = 'http://api.openweathermap.org/data/2.5/weather?q='+ville+'&units=metric&appid='+api_cle

requete = requests.get(url)
if requete.status_code == 200:
    print('Succès!')
elif requete.status_code == 404:
    print('Cette URL est introuvable.')
    exit()
temperature_json = requete.json()
print(temperature_json)
#{'coord': {'lon': -73.5878, 'lat': 45.5088}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
#'base': 'stations', 'main': {'temp': 22.15, 'feels_like': 21.7, 'temp_min': 20.98, 'temp_max': 23.44, 'pressure': 1022, 'humidity': 49},
#'visibility': 10000, 'wind': {'speed': 1.34, 'deg': 45, 'gust': 1.79}, 'clouds': {'all': 66}, 'dt': 1630087648, 'sys': {'type': 2, 'id': 2013133,
#'country': 'CA', 'sunrise': 1630059006, 'sunset': 1630107716}, 'timezone': -14400, 'id': 6077243, 'name': 'Montreal', 'cod': 200}

# Voici les prévisions pour aujourd'hui
print("Prévision pour aujourd'hui: " + temperature_json.get('weather')[0].get('description'))
print("Avec un minimum de " + str(temperature_json.get('main').get('temp_min')) + " degrés")
print("Et un maximum de " + str(temperature_json.get('main').get('temp_max')) + " degrés")



