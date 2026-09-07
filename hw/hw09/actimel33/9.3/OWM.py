from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(place, label):
    observation = mgr.weather_at_place(place)
    w = observation.weather

    status = w.detailed_status
    temp = w.temperature('celsius')['temp']
    wind_speed = w.wind()['speed']

    result_str = f"City: {place}\nConditions: {status}\nTemp: {temp}°C\nWind: {wind_speed} m/s"
    label['text'] = result_str



