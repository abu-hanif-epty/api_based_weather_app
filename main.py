import json
from pathlib import Path

from weather.geocoding import search_city
from weather.forecast import get_current_weather
from weather.display import show_weather
from weather.air_quality import get_air_quality
FAVORITES_FILE = Path("data/favorites.json")


def load_favorites():
    if not FAVORITES_FILE.exists():
        return []

    try:
        return json.loads(FAVORITES_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_favorite(city):
    favorites = load_favorites()

    favorite = {
        "name": city["name"],
        "country": city.get("country", ""),
        "latitude": city["latitude"],
        "longitude": city["longitude"],
    }

    if favorite not in favorites:
        favorites.append(favorite)
        FAVORITES_FILE.parent.mkdir(exist_ok=True)
        FAVORITES_FILE.write_text(
            json.dumps(favorites, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print("Favorite saved.")
    else:
        print("That city is already a favorite.")


def search_and_show_weather():
    print("-------------------------------------")
    city_name = input("Enter your city name: ").strip()
    if not city_name:
        print("Please enter a city name.")
        return

    matches = search_city(city_name)
    if not matches:
        print("No matching cities found.")
        return

    for number, city in enumerate(matches, start=1):
        print(f"{number}. {city['name']}, {city.get('country', '')}")

    try:
        choice = int(input("--Choose your city number: "))
        city = matches[choice - 1]
    except (ValueError, IndexError):
        print("That isn't a valid choice.")
        return

    weather = get_current_weather(city["latitude"], city["longitude"])
    show_weather(city, weather)

    if weather and input("Save as a favorite? (y/n): ").lower() == "y":
        save_favorite(city)


def show_favorites():
    favorites = load_favorites()
    if not favorites:
        print("You have no saved favorites yet.")
        return

    for city in favorites:
        weather = get_current_weather(city["latitude"], city["longitude"])
        show_weather(city, weather)


def check_air_quality():
    city_name = input("Enter a city name: ").strip()
    matches = search_city(city_name)

    if not matches:
        print("No matching cities found.")
        return

    for number, city in enumerate(matches, start=1):
        print(f"{number}. {city['name']}, {city.get('country', '')}")

    try:
        choice = int(input("Choose a city number: "))
        city = matches[choice - 1]
    except (ValueError, IndexError):
        print("That isn't a valid choice.")
        return
    hourly = get_air_quality(city["latitude"], city["longitude"])
    times = hourly.get("time", [])
    pm10_values = hourly.get("pm10", [])
    pm25_values = hourly.get("pm2_5", [])

    if not times:
        print("No air-quality data available.")
        return
    print("-----------------------------------------------------")
    print(f"Air quality for {city['name']} (first five hours):")
    for time, pm10, pm25 in zip(times[:5], pm10_values[:5], pm25_values[:5]):
        print(f"{time} | PM10: {pm10} ug/m3 | PM2.5: {pm25} ug/m3")
    print("-----------------------------------------------------")

def main():
    while True:
        print("\n============== Weather Information App ==============")
        print("1.Check weather by  City")
        print("2. Show favorite City ")
        print("3.Check air Quality by City")
        print("4.Exit")
        print("------------------------------")

        choice = input("Choose your option(1-4): ").strip()

        if choice == "1":
            search_and_show_weather()
        elif choice == "2":
            show_favorites()
        elif choice == "3":
            check_air_quality()
        elif choice == "4":
            print("=== Thank You So Much ===")
            break
        else:
            print("----------------------")
            print("==== !!NOTICE!! ====")
            print("CHOICE MUST (1-4)")
            print("----------------------")

if __name__ == "__main__":
    main()