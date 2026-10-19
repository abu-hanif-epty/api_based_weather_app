# api_based_weather_app

A Python command-line application that allows users to search for a city and view its current weather and air-quality information using Open-Meteo APIs.

This project was developed to practice Python fundamentals, API integration, JSON handling, and file operations through a practical project.

 ✨ Features

- **City Search:** Find cities by name using the Geocoding API.
- **Weather Information:** View temperature, humidity, wind speed, and weather conditions.
- **Air Quality:** Check hourly PM10 and PM2.5 readings.
- **Favorite Cities:** Save and view favorite cities using local JSON storage.
- **Persistent Data:** Keep saved cities available between application runs.

 🛠️ Technologies Used

- Python
- Requests library
- Open-Meteo APIs
- JSON for local data storage

 🔄 How It Works

The application finds a city's coordinates through the Geocoding API, then uses those coordinates to retrieve weather or air-quality data. The returned JSON responses are processed and displayed in the terminal.

🎯 Learning Objectives

- Making HTTP requests and working with API endpoints.
- Processing JSON responses.
- Reading and writing JSON files.
- Handling user input and organizing application logic.
- Building a practical command-line application.
 🌐 Data Sources

- [Open-Meteo Weather API](https://open-meteo.com/en/docs)
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)
- [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api)

👨‍💻 Author

Abu Hanif Epty 
A student of Artificial Intelligence learning Python development and API integration through hands-on projects.
