import requests
from typing import Optional

from util.constants import API_KEY


url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'


def get_data(query: str, location: str, radius: int) -> dict:
    params = {
        'query': query,
        'location': location,
        'radius': radius,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# get next data based on next page token
def get_next_data(next_page_token: Optional[str]) -> dict:
    if next_page_token is None:
        return {"status": "INVALID_NEXT_PAGE_TOKEN"}

    params = {
        'pagetoken': next_page_token,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data


# https://developers.google.com/maps/documentation/places/web-service/supported_types
