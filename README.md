# Weather & Quotes CLI 🌦️📜

A Python command-line application that fetches real-time weather data for a given city and displays a random inspirational quote.

## Features
- City-based weather lookup
- Real-time API data
- Random quote generation
- Graceful error handling
- Clean CLI output

## Tech Stack
- Python 3
- Requests
- Open-Meteo API
- ZenQuotes API

## Setup Instructions

```bash
git clone https://github.com/kai-devops/weather-and-quotes-cli.git
cd weather-and-quotes-cli
python -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
python main.py

example usage (prior to output) :
Enter a city: Cape Town
Fetching weather data...
Fetching quote...
