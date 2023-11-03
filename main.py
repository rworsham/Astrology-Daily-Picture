import streamlit as st
import requests

# Prepare API key and API url
api_key = "linqU7XYUbaWx1tk3GYOuQX9ss0M3du4uZgKPztS"
url = ("https://api.nasa.gov/planetary/"
       "apod?api_key=linqU7XYUbaWx1tk3GYOuQX9ss0M3du4uZgKPztS")

# Get the request data as dictionary
response = requests.get(url)
content = response.json()

# Extract the image title, url, and explanation
image_title = content['title']
image_url = content['url']
image_explanation = content['explanation']

# Download the image
image_path = "image.jpg"
image_content = requests.get(image_url)
with open(image_path, "wb") as file:
       file.write(image_content.content)

# Web Layout
st.title("Astrology Picture of the Day!")
st.header(image_title)
st.image(image_path)
st.write(image_explanation)