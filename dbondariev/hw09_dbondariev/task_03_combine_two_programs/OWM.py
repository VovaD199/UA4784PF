from pyowm import OWM


API_KEY = "12e1b191abdff87606e0c77d3175d166"

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(city, label):
    city = city.strip()

    if not city:
        label.config(text="Please enter a city name.")
        return

    try:
        observation = mgr.weather_at_place(city)
        weather = observation.weather

        temperature = weather.temperature("celsius")
        wind = weather.wind()

        result = (
            f"City: {city}\n"
            f"Status: {weather.detailed_status}\n"
            f"Temperature: {temperature['temp']} °C\n"
            f"Max temperature: {temperature['temp_max']} °C\n"
            f"Min temperature: {temperature['temp_min']} °C\n"
            f"Humidity: {weather.humidity}%\n"
            f"Wind speed: {wind.get('speed', 'N/A')} m/s\n"
            f"Clouds: {weather.clouds}%"
        )

        label.config(text=result)

    except Exception as error:
        label.config(
            text=(
                "Could not get weather.\n\n"
                "Try city format like:\n"
                "New York,US\n"
                "London,GB\n"
                "Lviv,UA\n"
                "Kyiv,UA\n\n"
                f"Error: {error}"
            )
        )
        print("Weather error:", error)