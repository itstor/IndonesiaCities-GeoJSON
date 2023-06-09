import pandas as pd
import json

df = pd.read_csv("list_location_id_csv.csv")

def format_kabko(kabko):
    kabko = kabko.replace("KAB.", "Kabupaten")
    words = kabko.split()
    words = [word.capitalize() for word in words]
    kabko = " ".join(words)
    return kabko

df["kabko"] = df["kabko"].apply(format_kabko)

features = []
for index, row in df.iterrows():
    feature = {}
    feature["type"] = "Feature"
    feature["properties"] = {"name": row["kabko"]}
    feature["geometry"] = {"type": "Point", "coordinates": [row["long"], row["lat"]]}
    features.append(feature)

geojson = {}
geojson["type"] = "FeatureCollection"
geojson["features"] = features

with open("cities.json", "w") as f:
    json.dump(geojson, f)