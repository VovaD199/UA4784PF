from pyowm import OWM


API_KEY = '9241c314f8a32eda28b84bb36d78349f'

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

print(w.detailed_status)         # 'clouds'
print(w.wind())                  # {'speed': 4.6, 'deg': 330}
print(w.humidity)                # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain)                    # {}
print(w.heat_index)              # None
print(w.clouds)                  # 75





