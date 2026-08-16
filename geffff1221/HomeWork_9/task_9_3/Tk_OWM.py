# Tk_OWM.py
import tkinter as tk
from OWM import get_weather_data

HEIGHT = 350
WIDTH = 450


def get_weather():
    city = entry_field.get()

    try:
        data = get_weather_data(city)
        result = (
            f"City: {city}\n"
            f"Status: {data['status']}\n"
            f"Temperature: {data['temp']}°C\n"
            f"Humidity: {data['humidity']}%\n"
            f"Wind speed: {data['wind_speed']} m/s"
        )
        label.config(text=result)

    except Exception as e:
        label.config(text="City not found or error occurred")


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                    text="Get Weather",
                    bg="gray", fg="white",
                    font=('Courier', 8),
                    command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()