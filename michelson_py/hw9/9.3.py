import tkinter as tk
from tkinter import messagebox
from pyowm import OWM

API_KEY = "8abf7cdfa6a7d16b9ada7960a1db5675"  


def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Помилка", "Будь ласка, введіть назву міста!")
        return

    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather

    
        status = w.detailed_status
        temp = w.temperature('celsius')['temp']
        humidity = w.humidity
        wind = w.wind()['speed']

        result_text = (
            f"Погода у місті {city.capitalize()}:\n\n"
            f"• Стан: {status.capitalize()}\n"
            f"• Температура: {temp}°C\n"
            f"• Вологість: {humidity}%\n"
            f"• Швидкість вітру: {wind} м/с"
        )
        result_label.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося отримати погоду для міста '{city}'.\nПеревірте назву або API-ключ.")

root = tk.Tk()
root.title("Прогноз погоди (OWM)")
root.geometry("400x350")
root.resizable(False, False)


title_label = tk.Label(root, text="Отримання погоди", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

city_label = tk.Label(input_frame, text="Місто:", font=("Arial", 12))
city_label.pack(side=tk.LEFT, padx=5)

city_entry = tk.Entry(input_frame, font=("Arial", 12), width=20)
city_entry.pack(side=tk.LEFT, padx=5)


get_btn = tk.Button(root, text="Отримати погоду", font=("Arial", 11), command=get_weather)
get_btn.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 11), justify=tk.LEFT, wraplength=350)
result_label.pack(pady=10)


if __name__ == "__main__":
        root.mainloop()
