import requests 
import sys
import os
from dotenv import load_dotenv

class WeatherApp:
    
    def __init__(self):
        load_dotenv()
        self.__url = os.getenv('URL')
        self.__api_key = os.getenv('API_KEY')

        if not self.__url or not self.__api_key:
            raise ValueError("URL and API_KEY environment variables are required")

    def current_weather(self,name):
        try:
            data = self.request(name)
            if data:
                location = data['location']
                current = data['current']

                location_data = {
                    'name': location['name'],
                    'country':location['country'],
                    'local_time': location['localtime']
                }

                weather_data = {
                    'temp_c':current['temp_c'],
                    'condition':current['condition']['text'],
                    'wind_speed(kph)': current['wind_kph'],
                    'wind_direction': current['wind_dir'],
                    'pressure(mb)': current['pressure_mb'],
                    'precipitation amount': current['precip_mm'],
                    'humidity': current['humidity'],
                    'feelslike_c': current['feelslike_c'],
                    'heatindex_c': current['heatindex_c'],
                    'dewpoint_c': current['dewpoint_c'],
                    'visibility': current['vis_km']
                }
                return location_data,weather_data
            else:
                raise ValueError('Empty Request')
        except ValueError as e:
            print(e)
            return None,None

    def request(self,name):
        try: 
            response = requests.get(self.__url,params=self.params(name))
            if response.status_code != 200:
                raise requests.exceptions.RequestException(
                    f"Failed to retrieve data. Status code: {response.status_code}"
                )
            return response.json()
        except requests.exceptions.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def params(self,name):
        params = {
            'key': self.__api_key,
            'q':name
        }
        return params


#test
# if __name__ == "__main__":
#     try:
#         weather_app = WeatherApp()

#         # Test with a city name
#         location_data, weather_data = weather_app.current_weather("London")

#         if location_data and weather_data:
#             print("Location Information:")
#             for key, value in location_data.items():
#                 print(f"  {key}: {value}")

#             print("\nWeather Information:")
#             for key, value in weather_data.items():
#                 print(f"  {key}: {value}")
#         else:
#             print("Failed to retrieve weather data")

#     except Exception as e:
#         print(f"Application error: {e}")

