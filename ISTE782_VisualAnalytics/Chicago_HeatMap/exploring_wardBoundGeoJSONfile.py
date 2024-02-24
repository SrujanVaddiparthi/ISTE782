import json

#loading the GeoJSON file

with open("/Users/wangtiles/ISTE782/ISTE782_VisualAnalytics/Chicago_HeatMap/ward_boundaries.geojson","r") as f:
    data = json.load(f)

#printing header contents
print("Header:")
print(data["features"][0]["properties"].keys())  #we assume all the features have the same properties

#print data for the first three rows
print("\nFirst three rows:")
for feature in data["features"][:3]:
    print(feature["properties"])



"""
#print the structure of the GeoJSON file
print(json.dumps(data,indent = 4))
"""
