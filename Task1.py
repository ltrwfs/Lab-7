import requests
import json


API_key = '99543fcf83dd955d992925d2271174a8'
city_name = 'Cherepovets'


def get_coord(city_name):
    geocoding_URL = (f'http://api.openweathermap.org/geo/1.0/'
                     +f'direct?q={city_name}&limit=1&appid={API_key}')
    response = requests.get(geocoding_URL)
    inf = json.loads(response.text)[0]
    return inf['lat'], inf['lon']


def get_weather(city_name):
    lat, lon = get_coord(city_name)
    weather_URL = (f'https://api.openweathermap.org/data/2.5/'
                   +f'weather?lat={lat}&lon={lon}&appid={API_key}')
    response = requests.get(weather_URL)
    inf = json.loads(response.text)
    weather = inf['weather'][0]['main']
    temp = int(inf['main']['temp']) - 273   #Converting Kelvin to Celcius
    hum = int(inf['main']['humidity'])
    press = int(inf['main']['pressure'])
    return weather, temp, hum, press


if __name__ == "__main__":
    weather, temp, hum, press = get_weather(city_name) 
    print(f'Weather in {city_name} now: {weather}, '
          +f'{temp}°C, humidity: {hum}%, pressure: {press} hPa')