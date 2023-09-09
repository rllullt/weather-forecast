import requests
import json

city = 'Huesca'

url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=es&appid=79d1ca96933b0328e1c7e3e7a26cb347'.format(city=city)

weather_data = requests.get(url).json()

# weather_data_structure = json.dumps(weather_data, indent=2)
# print(weather_data)

temp = round(weather_data['main']['temp'])
temp_feels = round(weather_data['main']['feels_like'])

print('Ahora en la ciudad de {city}: {temp} °C'.format(city=city, temp=temp))
print('Sensación térmica: {temp_feels} °C'.format(temp_feels=temp_feels))


