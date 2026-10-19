def describe_weather(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Rime fog",
        51: "Light drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        95: "Thunderstorm",
    }
    return descriptions.get(code, "Other conditions")


def show_weather(city, weather):
    if not weather:
        print("No weather data available.")
        return
    print("--------------------------------------------")
    print(f"   Weather for {city['name']}")
    print(f"   Temperature: {weather.get('temperature_2m')} °C")
    print(f"   Humidity: {weather.get('relative_humidity_2m')}%")
    print(f"   Wind speed: {weather.get('wind_speed_10m')} km/h")
    print(f"   Conditions: {describe_weather(weather.get('weather_code'))}")
    print("---------------------------------------------")