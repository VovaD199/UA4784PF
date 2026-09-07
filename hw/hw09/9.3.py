import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(Surface,place):
    observation = mgr.weather_at_place(place)
    weather = observation.weather
    wind = weather.wind()
    t = weather.temperature("celsius")
    text = f'detailed status: {weather.detailed_status}\n'+\
            f'wind speed: {wind["speed"]}\n'+\
            f'wind degree: {wind["deg"]}\n'+\
            f'wind gust: {wind["gust"]}\n'+\
            f'humidity: {weather.humidity}\n'+\
            f'temperature (celsius): {t["temp"]}\n'+\
            f'max temperature (celsius): {t["temp_max"]}\n'+\
            f'min temperature (celsius): {t["temp_min"]}\n'+\
            f'feels like (celsius): {t["feels_like"]}\n'+\
            f'heat index: {weather.heat_index}\n'+\
            f'clouds percentage: {weather.clouds}\n'
    Surface.config(text = text)
    return None
    


HEIGHT = 600
WIDTH = 800


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14),text="ABRACADABRA!!! (enter the location to view weather)",anchor='w',justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(label,entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

root.mainloop()

