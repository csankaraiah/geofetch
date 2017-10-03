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


df = pd.read_csv('LV_address_spit.csv')
df



gmaps = googlemaps.Client(key='AIzaSyDednPA5ssSnBus0hJOvySyzehMUtLCM0A')
# Geocoding an address
geocode_result = gmaps.geocode('5315 10th ave s minneapolis mn')

print type(geocode_result)
print len(geocode_result)
print geocode_result

json_result = json.dumps(geocode_result[0])

json_r1 = json.loads(json_result)

#json_result1 = json.load(geocode_result[0])
print json_result
print type(json_result)
print json_r1
print type(json_r1)
print type(json_r1["address_components"])
print json_r1["address_components"][7]["short_name"]


#print json_result['geometry']

    ## Google location code API key
## AIzaSyD_WFbcLN4xJPCNkq7n7ii-xvP5kaXJrvc
## AIzaSyDednPA5ssSnBus0hJOvySyzehMUtLCM0A