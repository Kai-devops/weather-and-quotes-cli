from src.weather import get_weather
from src.quotes import get_random_quote
from src.utils import print_divider


def main():
    city = input("Enter a city: ").strip()

    try:
        print("Fetching weather data...")
        weather = get_weather(city)

        print("Fetching quote...")
        quote, author = get_random_quote()

        print_divider()
        print(f"Weather in {city.title()}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")

        print_divider()
        print("Quote of the moment:")
        print(f"\"{quote}\"")
        print(f"- {author}")
        print_divider()

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
