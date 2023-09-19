import requests
import json
import time

# Ganti dengan API key Anda
api_key = ''

# Koordinat batas wilayah (lat dan long)
southwest = '-6.832462, 105.210232'  # Koordinat sudut barat daya
northeast = '-6.250752, 106.180119'  # Koordinat sudut timur laut
# -6.399163,105.996395|-6.834324,105.214889

# Koordinat tengah wilayah
location = '-6.588535,105.795815'
radius = 50000  # Jarak dalam meter

# Teks pencarian
query = 'smp'  # Teks yang ingin Anda cari

# URL API Google Place
url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location}&radius={radius}&key={api_key}'

# Mengirim permintaan ke API Google
response = requests.get(url)

# Mendapatkan data JSON sebagai respons
data = response.json()

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
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}'
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
