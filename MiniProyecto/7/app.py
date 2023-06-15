from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_weather_data():
    url = "https://www.meteored.mx/clima_Monterrey-America+Norte-Mexico-Nuevo+Leon-MMMY-1-21045.html"

    # Realizar la solicitud GET a la página web
    response = requests.get(url)
    response.raise_for_status()

    # Crear el objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer la información del clima
    ubicacion = soup.select_one('.titulo').get_text(strip=True)
    descripcion = soup.select_one('.descripcion').get_text(strip=True)
    temperature = soup.select_one('.dato-temperatura').get_text(strip=True)
    condition = soup.select_one('.sensacion').get_text(strip=True)

    return descripcion, ubicacion, temperature, condition

@app.route('/')
def home():
    descripcion, ubicacion, temperature, condition = scrape_weather_data()
    return render_template('index.html', ubicacion =ubicacion, descripcion=descripcion, temperature=temperature, condition=condition)

if __name__ == '__main__':
    app.run()

