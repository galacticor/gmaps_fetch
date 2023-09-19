import requests
import json
import time

from core.text_search import get_data


# Koordinat batas wilayah (lat dan long)
southwest = '-6.832462, 105.210232'  # Koordinat sudut barat daya
northeast = '-6.250752, 106.180119'  # Koordinat sudut timur laut
# -6.399163,105.996395|-6.834324,105.214889

# Koordinat tengah wilayah
location = '-6.588535,105.795815'
radius = 10000  # Jarak dalam meter

# Teks pencarian
query = 'smp'  # Teks yang ingin Anda cari

data = get_data(query, location, radius)

def main():
    locations = [
        '-6.588535,105.795815',
    ]

    for loc in locations:
        data = get_data(query, loc, radius)
        if data['status'] == 'OK':
            for place in data['results']:
                print(f"Nama Tempat: {place['name']}")
                print(f"Alamat: {place['formatted_address']}")
                print(f"Koordinat: Lat {place['geometry']['location']['lat']} Long {place['geometry']['location']['lng']}")
                print('-' * 50)
        else:
            print("Tidak ada hasil ditemukan atau ada masalah dengan permintaan Anda.")

res = []
while data['status'] == 'OK':
    # breakpoint()
    if len(data['results']) == 0:
        break
    
    print(len(data['results']))
    for place in data['results']:
        print(f"Nama Tempat: {place['name']}")
        print(f"Alamat: {place['formatted_address']}")
        print(f"Koordinat: Lat {place['geometry']['location']['lat']} Long {place['geometry']['location']['lng']}")
        print('-' * 50)

        res.append(place)

        # URL API Google Place
        # url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location}&radius={radius}&key={api_key}'
    time.sleep(2.5)
    next_page_token = data['next_page_token']
    print(next_page_token)
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={API_KEY}'
    # Mengirim permintaan ke API Google
    response = requests.get(url)

    # Mendapatkan data JSON sebagai respons
    data = response.json()
    print(data['status'])

json.dump(res, open('data.json', 'w'))


# Menampilkan hasil pencarian
# if data['status'] == 'OK':
#     for place in data['results']:
#         print(f"Nama Tempat: {place['name']}")
#         print(f"Alamat: {place['formatted_address']}")
#         print(f"Koordinat: Lat {place['geometry']['location']['lat']} Long {place['geometry']['location']['lng']}")
#         print('-' * 50)
# else:
#     print("Tidak ada hasil ditemukan atau ada masalah dengan permintaan Anda.")
