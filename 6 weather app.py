from requests import request
import json 

api_key = '6ad30eb2cf7b076062174723014b8baf'
city = 'Ho Chi Minh'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
payload = {}
headers = {}

response = request('GET',url).text
parsed = json.loads(response)
# print(json.dumps(parsed, indent=4, sort_keys = True))
# printarsed)
print(f'Weather: {parsed["weather"][0]["main"]}')
print(f'Temperature: {round(parsed["main"]["feels_like"] - 273.15, 2)}°C')
