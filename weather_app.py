import requests

def get_weather(city):
    API_KEY = "afe2cd88f06e46630bad203a77ba243d"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print(f"Error fetching weather data for {city}. Reason: {data.get('message', 'Unknown error')}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
