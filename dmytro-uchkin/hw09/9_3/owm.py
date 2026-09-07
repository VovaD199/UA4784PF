from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75


def get_weather(location: str) -> str:
    try:
        observation = mgr.weather_at_place(location)
        w = observation.weather

        temp = w.temperature("celsius")
        wind = w.wind()
        rain = w.rain.get("1h", 0)

        return (
            f"Location: {location}\n"
            f"Weather: {w.detailed_status}\n"
            f"Temperature: {temp['temp']}°C "
            f"(min {temp['temp_min']}°C, max {temp['temp_max']}°C)\n"
            f"Humidity: {w.humidity}%\n"
            f"Wind: {wind['speed']} m/s, {wind.get('deg', 'N/A')}°\n"
            f"Clouds: {w.clouds}%\n"
            f"Rain (last hour): {rain} mm"
        )

    except Exception:
        return "Invalid location"
