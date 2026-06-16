import os
import requests
from django.core.management.base import BaseCommand
from blog.models import WeatherData
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Obtiene datos del clima y los guarda en la base de datos'

    def handle(self, *args, **kwargs):
        api_key = os.environ.get('OPENWEATHER_API_KEY')
        city = 'Bogota'
        url = 'https://api.openweathermap.org/data/2.5/weather'

        try:
            response = requests.get(url, params={
                'q': city,
                'appid': api_key,
                'units': 'metric',
                'lang': 'es'
            })
            response.raise_for_status()
            data = response.json()

            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            WeatherData.objects.create(
                city=city,
                temperature=temperature,
                description=description
            )

            self.stdout.write(self.style.SUCCESS(
                f'Clima guardado: {city} - {temperature}°C - {description}'
            ))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error al obtener clima: {e}'))