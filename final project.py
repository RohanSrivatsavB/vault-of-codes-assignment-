from cgi import print_arguments
import tkinter as tk
import requests

# OpenWeatherMap API
API_KEY = '92a0479f304d64e70eda4edf4f6a9222'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Emojis for different weather conditions
weather_emojis = {
    'Clear': '☀️',
    'Clouds': '☁️',
    'Rain': '🌧️',
    'Snow': '❄️',
    'Thunderstorm': '⛈️',
    'Drizzle': '🌦️',
    'Mist': '🌫️',
    'Smoke': '💨',
    'Haze': '🌫️',
    'Dust': '💨',
    'Fog': '🌫️',
    'Sand': '💨',
    'Ash': '💨',
    'Squall': '💨',
    'Tornado': '🌪️'
}

def get_weather(city):
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY})
    weather_data = response.json()

    if weather_data['cod'] == 200:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temp_kelvin = weather_data['main']['temp']
        temp_celsius = round(temp_kelvin - 273.15, 2)
        weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        lbl_location.config(text=f'{city}, {country} {weather_emojis.get(weather, "")}')
        lbl_temperature.config(text=f'Temperature: {temp_celsius} °C')
        lbl_weather.config(text=f'Weather: {weather}')
        lbl_description.config(text=f'Description: {description}')
        lbl_humidity.config(text=f'Humidity: {humidity}%')
        lbl_wind_speed.config(text=f'Wind Speed: {wind_speed} m/s')
    else:
        print_arguments('Error', f'Cannot find city: {city} 😞')

def search():
    get_weather(txt_city.get())

root = tk.Tk()
root.title('Weather App ☀️☁️🌧️')

txt_city = tk.Entry(root, font=('Helvetica', 24))
txt_city.pack(pady=20)

btn_search = tk.Button(root, text='Search 🔍', command=search, font=('Helvetica', 20))
btn_search.pack()

lbl_location = tk.Label(root, font=('Helvetica', 22), fg='blue')
lbl_location.pack()

lbl_temperature = tk.Label(root, font=('Helvetica', 24), fg='red')
lbl_temperature.pack()

lbl_weather = tk.Label(root, font=('Helvetica', 22), fg='green')
lbl_weather.pack()

lbl_description = tk.Label(root, font=('Helvetica', 22), fg='purple')
lbl_description.pack()

lbl_humidity = tk.Label(root, font=('Helvetica', 22), fg='orange')
lbl_humidity.pack()

lbl_wind_speed = tk.Label(root, font=('Helvetica', 22), fg='brown')
lbl_wind_speed.pack()

root.mainloop()
