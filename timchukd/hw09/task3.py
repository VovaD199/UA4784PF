"""
Task 3.
You need to combine two programs OWM.py and Tk_OWM.py
into one working program.
"""
import tkinter as tk
from pyowm import OWM

# -------------------------
# OpenWeatherMap settings
# -------------------------

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# -------------------------
# Tkinter settings
# -------------------------

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# -------------------------
# Get weather function
# -------------------------

def get_weather():
    city = entry_field.get()

    try:
        observation = mgr.weather_at_place(city)
        weather = observation.weather

        temperature = weather.temperature('celsius')
        wind = weather.wind()

        weather_info = (
            f"City: {city}\n\n"
            f"Weather: {weather.detailed_status}\n"
            f"Temperature: {temperature['temp']} °C\n"
            f"Min temperature: {temperature['temp_min']} °C\n"
            f"Max temperature: {temperature['temp_max']} °C\n"
            f"Humidity: {weather.humidity}%\n"
            f"Wind speed: {wind['speed']} m/s\n"
            f"Clouds: {weather.clouds}%"
        )

        label.config(text=weather_info)

    except Exception:
        label.config(
            text="City not found.\nPlease enter a valid city name."
        )


# -------------------------
# Search frame
# -------------------------

frame = tk.Frame(
    root,
    bg="deep sky blue",
    bd=5
)

frame.place(
    relx=0.5,
    rely=0.1,
    relwidth=0.75,
    relheight=0.1,
    anchor='n'
)


entry_field = tk.Entry(
    frame,
    font=('Courier', 12)
)

entry_field.place(
    relx=0,
    rely=0,
    relwidth=0.65,
    relheight=1
)


button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=('Courier', 8),
    command=get_weather
)

button.place(
    relx=0.7,
    rely=0,
    relwidth=0.3,
    relheight=1
)

# -------------------------
# Weather result frame
# -------------------------

lower_frame = tk.Frame(
    root,
    bg='gold',
    bd=10
)

lower_frame.place(
    relx=0.5,
    rely=0.25,
    relwidth=0.75,
    relheight=0.6,
    anchor='n'
)


label = tk.Label(
    lower_frame,
    font=('Courier', 14),
    justify='left'
)

label.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
)

# -------------------------
# Start application
# -------------------------

root.mainloop()