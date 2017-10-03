import googlemaps
import json
import csv
import pandas as pd
import numpy as np

gmaps = googlemaps.Client(key='AIzaSyDednPA5ssSnBus0hJOvySyzehMUtLCM0A')

def get_zipcode(addr):
    geocode_result = gmaps.geocode(addr)
    json_result = json.loads(json.dumps(geocode_result[0]))
    zipcode = json_result["address_components"][7]["short_name"]
    return zipcode




data = pd.read_csv('LV_address_spit.csv', dtype = {'Name': str,'Address':str,'City': str,'State': str,'Zip': str,'Ward':str,'Number':str, 'Contacted':str, 'Placed':str}, engine = 'c')
i = 0
for index, row in data.iterrows():
    #addr = row["Address"] + row["City"] + row["State"]
    addr = row['Address'][i] + row['City'][i] + row['State'][i]
    if i < 3:
        i = i + 1