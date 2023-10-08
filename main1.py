import requests
import json
import time

from core.convert_data import Place, print_data
from core.text_search import get_data, get_next_data


# Koordinat batas wilayah (lat dan long)
southwest = '-6.832462, 105.210232'
northeast = '-6.250752, 106.180119'
# -6.399163,105.996395|-6.834324,105.214889

# Koordinat tengah wilayah
location = '-6.588535,105.795815'
radius = 10000  # Jarak dalam meter

# Teks pencarian
query = 'sd'  # Teks yang ingin Anda cari

def main():
    locations = [
        '-6.588535,105.795815',
    ]

    res = []
    names = set()

    for loc in locations:
        data = get_data(query, loc, radius)

        while data['status'] == 'OK':
            if len(data['results']) == 0:
                break
            
            for place in data['results']:
                place = Place.from_dict(place)
                if "Pandeglang" not in place.address or place.name in names:
                    continue

                res.append(place)
                print_data(place)

                names.add(place.name)

            print(f"Total: {len(res)}")

            time.sleep(2.5)
            next_page_token = data.get('next_page_token')
            # print(next_page_token)
            data = get_next_data(next_page_token)

        else:
            print("Tidak ada hasil ditemukan atau ada masalah dengan permintaan Anda.")

    with open(f'./result/data_{query}.csv', 'w') as f:
        f.write('WKT,name,address\n')
        for place in res:
            f.write(f"{place.to_csv()}\n")


if __name__ == '__main__':
    main()
