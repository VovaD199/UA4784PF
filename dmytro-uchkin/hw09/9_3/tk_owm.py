import tkinter as tk
from tkinter import *
from owm import get_weather

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")
root.geometry(f"{WIDTH}x{HEIGHT}")


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="red", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


weather_info = StringVar(value="Welcome in Weather Application")

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=("Courier", 8),
    command=lambda: weather_info.set(get_weather(entry_field.get())),
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")


label = tk.Label(
    lower_frame,
    textvariable=weather_info,
    font=("Courier", 14),
    anchor="nw",
    justify="left",
)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()