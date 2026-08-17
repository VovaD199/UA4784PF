import tkinter as tk
from pyowm import OWM


API_KEY = "ef2206ff5da67de63306d0b143e20872"

HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)
weather_manager = owm.weather_manager()


def get_weather():
    city = entry_field.get().strip()

    if not city:
        label.config(text="Enter a city name.")
        return

    try:
        observation = weather_manager.weather_at_place(city)
        weather = observation.weather

        temperature = weather.temperature("celsius")
        wind = weather.wind()

        result = (
            f"City: {city}\n"
            f"Status: {weather.detailed_status}\n"
            f"Temperature: {temperature['temp']} °C\n"
            f"Humidity: {weather.humidity}%\n"
            f"Wind speed: {wind['speed']} m/s\n"
            f"Clouds: {weather.clouds}%"
        )

        label.config(text=result)

    except Exception:
        label.config(text="City not found or connection error.")


root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(
    relx=0.5,
    rely=0.1,
    relwidth=0.75,
    relheight=0.1,
    anchor="n"
)

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=("Courier", 8),
    command=get_weather
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(
    relx=0.5,
    rely=0.25,
    relwidth=0.75,
    relheight=0.6,
    anchor="n"
)

label = tk.Label(
    lower_frame,
    font=("Courier", 12),
    justify="left"
)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()