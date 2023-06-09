import pandas as pd
import json

df = pd.read_csv("worldcities.csv")

df = df[df["country"] == "Indonesia"]

features = []
for index, row in df.iterrows():
    feature = {}
    feature["type"] = "Feature"
    feature["properties"] = {"city": row["city"]}
    feature["geometry"] = {"type": "Point", "coordinates": [row["lng"], row["lat"]]}
    features.append(feature)

geojson = {}
geojson["type"] = "FeatureCollection"
geojson["features"] = features

with open("cities.json", "w") as f:
    json.dump(geojson, f)