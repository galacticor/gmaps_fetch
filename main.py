import googlemaps
from datetime import datetime

API_KEY = ""

gmaps = googlemaps.Client(key=API_KEY)

x = gmaps.places(
    "restaurant",
    location=(-6.588535, 105.795815),
    radius=2000,
    region="ID",
    language="ID",
    min_price=1,
    max_price=4,
    open_now=True,
    # type=self.type,
)

print(x)


