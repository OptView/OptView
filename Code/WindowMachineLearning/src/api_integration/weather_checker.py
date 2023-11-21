import requests
from dotenv import load_dotenv
import os


class WeatherChecker:
    def __init__(self, api_key):
        """Initialize the WeatherChecker with the API key.

        Args:
            api_key (str): The OpenWeatherMap API key.
        """
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.api_key = api_key

    def construct_url(self, city):
        """Construct the URL for the API request.

        Args:
            city (str): The city to check the weather for.

        Returns:
            str: The constructed URL.
        """
        return self.base_url + "appid=" + self.api_key + "&q=" + city

    def fetch_data(self, url):
        """Fetch the weather data from the API.

        Args:
            url (str): The URL to make the request to.

        Returns:
            dict: The JSON response from the API.
        """
        response = requests.get(url)
        return response.json()

    def check_weather_conditions(self, city):
        """Check the weather conditions for the specified city.

        Args:
            city (str): The city to check the weather for.

        Returns:
            int: 0 if the weather condition is found and reported, 1 otherwise.
        """
        url = self.construct_url(city)
        data = self.fetch_data(url)

        if data["cod"] != 200:
            print("Error:", data["cod"], ".", data["message"])
            return 1

        weather_condition = data["weather"][0]["main"]

        condition_messages = {
            "Rain": f"It's raining in {city}.",
            "Snow": f"It's snowing in {city}.",
            "Thunderstorm": f"There's a thunderstorm in {city}.",
            "Dust": f"There's dust in the air in {city}."
        }

        if weather_condition in condition_messages:
            print(condition_messages[weather_condition])
            return 0
        else:
            print(f"The weather in {city} is currently {weather_condition}.")
            return 1


# Example usage:
load_dotenv()
api_key = os.getenv('WEATHER_API_KEY')  # Get API key from environment variable
weather_checker = WeatherChecker(api_key)
city = "Edinburgh"
weather_checker.check_weather_conditions(city)
