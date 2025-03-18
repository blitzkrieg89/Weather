from tkinter import *
from PIL import ImageTk, Image
import requests
import json
root = Tk()
root.title("Weather Forecasting")
root.geometry("1920x1080")

# Add background image
bg_image = Image.open('background img.jpg')
bg_image = bg_image.resize((1920,1080), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)
canvas = Canvas(root, width=1920, height=1080)
canvas.create_image(0, 0, anchor=NW, image=bg_image)
canvas.pack()

# Add title label
title_label = Label(root, text="Enter Location", font=("Times New Roman",
30,"bold"), bg="#b05c45", fg="black", width=30)
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Add location entry box
location_entry = Entry(root, font=("Bell MT", 18), width=18)
location_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

# Function to get weather data from API
def get_weather():
    api_key = "c3e16b425823385a6a90efa59dc5e3bc"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = location_entry.get()

    if not city_name:
        output_label.config(text="Please enter a location!")
        return

    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    data = response.json()

    if response.status_code != 200:
        output_label.config(text="City not found. Try again!")
        return

    temperature = round((data['main']['temp'] - 273.15), 2)
    feels_like = round((data['main']['feels_like'] - 273.15), 2)
    pressure = round((data['main']['pressure']), 2)
    wind_speed = round(data['wind']['speed'], 2)
    weather_description = data['weather'][0]['description']

    output_label.config(text=(
        f"Temperature: {temperature}°C\n"
        f"Feels Like: {feels_like}°C\n"
        f"Pressure: {pressure} hPa\n"
        f"Wind Speed: {wind_speed} kmph\n"
        f"Description: {weather_description}"
    ))

# Add get weather button
get_weather_button = Button(root, text="Get Weather", font=("Bell MT", 14),
bg="#b05c45", fg="black", width=15, command=get_weather)
get_weather_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# Add output label
output_label = Label(root, font=("Bell MT", 20), bg="#b05c45", fg="black",
width=35, height=7)
output_label.place(relx=0.5, rely=0.85, anchor=CENTER)

root.mainloop()