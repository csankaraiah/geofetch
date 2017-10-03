import googlemaps
import json
import csv

gmaps = googlemaps.Client(key='AIzaSyDednPA5ssSnBus0hJOvySyzehMUtLCM0A')

try:
    def get_zipcode(addr):
        geocode_result = gmaps.geocode(addr)
        try:
            json_result = json.loads(json.dumps(geocode_result[0]))
        except IndexError:
            json_result = [0]
            zipcode = 'null'
        try:
            zipcode = json_result["address_components"][7]["short_name"]
        except IndexError:
            zipcode = 'null'
        return zipcode
except IndexError:
    zipcode = 'null'

with open("LV_address_spit_5.csv") as f:
    addr = csv.reader(f)
    for col1 in addr:
        value = str(col1)
        zipcode = get_zipcode(value)
        print col1[0], ',', zipcode