
import requests

API_KEY = "ac137ecf7002a74e81060248245e83b0"
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    weather = {
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "desc": data['weather'][0]['description']
    }
    
    return weather