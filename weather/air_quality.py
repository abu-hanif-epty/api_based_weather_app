import requests


def get_air_quality(latitude, longitude):
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "pm10,pm2_5",
        "forecast_days": 1,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("hourly", {})
    except requests.exceptions.RequestException as error:
        print(f"Could not get air quality: {error}")
        return {}