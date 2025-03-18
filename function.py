import requests
def get_weather_data(location, api_key):
 api_key = "c3e16b425823385a6a90efa59dc5e3bc"
 url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
 response = requests.get(url)
 data = response.json()
 weather = {
 "description": data["weather"][0]["description"],
 "temperature": data["main"]["temp"],
 "feels_like": data["main"]["feels_like"],
 "humidity": data["main"]["humidity"],
 "pressure": data["main"]["pressure"],
 "wind_speed": data["wind"]["speed"],
 "wind_direction": data["wind"]["direction"],
 }
 return weather