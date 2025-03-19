import streamlit as st
from PIL import Image
import requests

# Set up the Streamlit app
st.set_page_config(page_title="Weather Forecasting", layout="wide")

# Load and display background image
bg_image_path = "C:\Users\Admin\Downloads\weatherimage.jpeg"

try:
    bg_image = Image.open(bg_image_path)
    st.image(bg_image, use_column_width=True)
except Exception as e:
    st.error(f"Error loading background image: {e}")

# Title of the app
st.markdown("<h1 style='text-align: center; color: black;'>Weather Forecasting</h1>", unsafe_allow_html=True)

# Input field for the city
city_name = st.text_input("Enter Location:", "")

# API Key and Base URL
API_KEY = "c3e16b425823385a6a90efa59dc5e3bc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Function to fetch weather data
def get_weather(city):
    if not city:
        return "Please enter a location!", None
    
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city}"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if "main" not in data:
            return "City not found. Try again!", None

        weather_data = {
            "Temperature": f"{round(data['main']['temp'] - 273.15, 2)}°C",
            "Feels Like": f"{round(data['main']['feels_like'] - 273.15, 2)}°C",
            "Pressure": f"{data['main']['pressure']} hPa",
            "Wind Speed": f"{round(data['wind']['speed'], 2)} km/h",
            "Description": data['weather'][0]['description'].capitalize()
        }

        return None, weather_data
    except requests.exceptions.RequestException as e:
        return "Error fetching weather data.", None

# Button to fetch weather
if st.button("Get Weather"):
    error_msg, weather_info = get_weather(city_name)
    
    if error_msg:
        st.error(error_msg)
    else:
        st.success("Weather data fetched successfully!")
        st.json(weather_info)  # Display weather data as a JSON format
