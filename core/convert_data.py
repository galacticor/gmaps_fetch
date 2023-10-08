from dataclasses import dataclass


@dataclass
class Place:
    name: str
    address: str
    lat: float
    lng: float

    @staticmethod
    def from_dict(place: dict):
        name = place['name']
        address = place['formatted_address']
        lat = place['geometry']['location']['lat']
        lng = place['geometry']['location']['lng']

        return Place(name, address, lat, lng)

    def to_kml(self):
        return f"<Placemark><name>{self.name}</name><description>{self.address}</description><Point><coordinates>{self.lng},{self.lat}</coordinates></Point></Placemark>"

    def to_csv(self):
        return f'"POINT ({self.lng} {self.lat})","{self.name}","{self.address}"'

    def to_json(self):
        return {
            'name': self.name,
            'address': self.address,
            'lat': self.lat,
            'lng': self.lng
        }


def print_data(place: Place):
    print(f"Nama Tempat: {place.name}")
    print(f"Alamat: {place.address}")
    print(f"Koordinat: Lat {place.lat} Long {place.lng}")
    print('-' * 50)


# convert data from place dict to google mymaps kml format
def convert_data(place: dict) -> str:
    name = place['name']
    address = place['formatted_address']
    lat = place['geometry']['location']['lat']
    lng = place['geometry']['location']['lng']

    return f"<Placemark><name>{name}</name><description>{address}</description><Point><coordinates>{lng},{lat}</coordinates></Point></Placemark>"


# convert data from place dict to google mymaps csv format


