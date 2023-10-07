

def print_data(place: dict):
    print(f"Nama Tempat: {place['name']}")
    print(f"Alamat: {place['formatted_address']}")
    print(f"Koordinat: Lat {place['geometry']['location']['lat']} Long {place['geometry']['location']['lng']}")
    print('-' * 50)
