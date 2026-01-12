import requests


def get_weather(city):
    """
    Fetch current weather data for a given city using Open-Meteo.
    """
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"

    geo_response = requests.get(
        geocode_url,
        params={"name": city, "count": 1},
        timeout=10
    )
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if not geo_data.get("results"):
        raise ValueError("City not found or API unavailable")


    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    weather_response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True
        },
        timeout=5
    )
    weather_response.raise_for_status()

    return weather_response.json()["current_weather"]
