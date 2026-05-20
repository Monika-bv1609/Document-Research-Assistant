import os
import requests

from dotenv import load_dotenv

# Load env variables
load_dotenv()


def get_weather(
    city: str
):

    try:

        api_key = os.getenv(
            "WEATHER_API_KEY"
        )

        # Weather API URL
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={api_key}"
            f"&units=metric"
        )

        # Send GET request
        response = requests.get(url)

        # Convert to JSON
        data = response.json()

        print(data)

        # Extract details
        temperature = data["main"]["temp"]

        weather = data["weather"][0]["description"]

        return (
            f"Weather in {city}: "
            f"{temperature}°C, {weather}"
        )

    except Exception as e:

        print(e)

        return "Weather information not found."