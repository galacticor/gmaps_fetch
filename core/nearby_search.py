import requests


url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'


def get_data(query: str, location: str, radius: int, api_key: str):
    params = {
        'query': query,
        'location': location,
        'radius': radius,
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data
