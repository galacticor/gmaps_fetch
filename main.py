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
radius = 5000  # Jarak dalam meter

# Teks pencarian
query = 'sd'  # Teks yang ingin Anda cari

def main():
    locations = [
        '-6.588535,105.795815',
        '-6.790689, 105.548599',
        '-6.560176, 105.672195',
        '-6.437374, 105.901535',
        '-6.345936, 106.000411',
        '-6.689768, 105.823257',
        '-6.747050, 105.316513',
    ]

    res = []
    names = set()

    with open(f'./result/data_{query}.csv', 'w', encoding="utf-8") as f:
        f.write('WKT,name,address\n')

    for i, loc in enumerate(locations):
        data = get_data(query, loc, radius)

        while data['status'] == 'OK':
            if len(data['results']) == 0:
                break

            new_loc = None

            for place in data['results']:
                place = Place.from_dict(place)
                place.address = place.address.replace('"', '')
                if "Pandeglang" not in place.address or place.name in names:
                    continue

                res.append(place)
                print_data(place)

                names.add(place.name)
                new_loc = f"{place.lat},{place.lng}"

                with open(f'./result/data_{query}.csv', 'a', encoding="utf-8") as f:
                    f.write(f"{place.to_csv()}\n")

            print(f"Total: {len(res)}")

            if new_loc is not None: locations.append(new_loc)

            time.sleep(2.5)
            next_page_token = data.get('next_page_token')
            # print(next_page_token)
            data = get_next_data(next_page_token)

        else:
            print(f"Done for location {loc}, left {len(locations) - i - 1} locations")


if __name__ == '__main__':
    main()
