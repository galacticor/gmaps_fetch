import requests

from util.constants import API_KEY


url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'


def get_data(query: str, location: str, radius: int):
    params = {
        'query': query,
        'location': location,
        'radius': radius,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


# https://developers.google.com/maps/documentation/places/web-service/supported_types
