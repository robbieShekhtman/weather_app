import requests ##query internet
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv("API_KEY")


@dataclass
class weatherInfo:
    condition : str
    temp : str
    icon : str
    feelsLike: str
    precip: str


def get_curr(city, key):
    resp = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no").json()

    info = weatherInfo(
        condition = resp.get('current').get('condition').get('text'),
        temp = str(resp.get('current').get('temp_f')),
        icon = resp.get('current').get('condition').get('icon'),
        feelsLike = resp.get('current').get('feelslike_f'),
        precip = resp.get('current').get('precip_in'))


    
    return info

def main(city):
    return get_curr(city, api_key)

if __name__ == "__main__":
    print(get_curr("London", api_key))
 