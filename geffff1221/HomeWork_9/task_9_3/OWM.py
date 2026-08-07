from pyowm import OWM

API_KEY = '22d5cc79c1c8df6acceeee6aa9571519'
owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather_data(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather

    return {
        "status": w.detailed_status,
        "temp": w.temperature('celsius')['temp'],
        "humidity": w.humidity,
        "wind_speed": w.wind()['speed']
    }

