import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

ch_number = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(ch_number, "en")
print(yourLocation)

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

GKey = "a845f1e7333c4b67a5abfaffe1674850"
geocoder = OpenCageGeocode(GKey)

query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)
