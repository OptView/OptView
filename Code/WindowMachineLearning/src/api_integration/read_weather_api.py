import requests
from dotenv import load_dotenv


def check_weather_conditions(city, api_key):
    # Construct the URL

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    final_url = base_url + "appid=" + api_key + "&q=" + city

    # Fetch the data
    response = requests.get(final_url)
    data = response.json()

    # Check if the request was successful
    if data["cod"] != 200:
        print("Error:", data["cod"], ".", data["message"])
        return None

    # Check weather condition
    weather_condition = data["weather"][0]["main"]

    # Map conditions to messages
    condition_messages = {
        "Rain": f"It's raining in {city}.",
        "Snow": f"It's snowing in {city}.",
        "Thunderstorm": f"There's a thunderstorm in {city}.",
        "Dust": f"There's dust in the air in {city}."
    }

    # Check and print the message for the current weather condition
    if weather_condition in condition_messages:
        print(condition_messages[weather_condition])
        return 0
    elif weather_condition:  # Other weather conditions not in our map
        print(f"The weather in {city} is currently {weather_condition}.")
        return 1
    else:
        print(f"Couldn't fetch weather data for {city}.")
        return 1

city = "Edinburgh"
api_key = os.getenv('WEATHER_API_KEY')  # Get API key from environment variable

check_weather_conditions(city, api_key)
