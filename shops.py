#!/usr/bin/python3

import json
import sys
from datetime import date

brand = sys.argv[1]

def unpack_shop(shop):
  if brand=="zabka":
    lat = shop["lat"]
    lon = shop["lng"]
    label = shop["id"]
  elif brand=="rossmann":
    coords = shop["shopLocation"]
    lat = coords["latitude"]
    lon = coords["longitude"]
    addr = shop["address"]
    label = f"{addr['city']}, {addr['street']}"
  elif brand=="moya":
    if shop["type"]!=1: # 1 stands for station with human personel
      return None

    lat = shop["lat"]
    lon = shop["lng"]
    label = f"{shop['city']}, {shop['address']}"
  else:
    raise Exception(f"Unknown brand {brand}")

  return lat, lon, label

shops = json.load(sys.stdin)

today = date.today().isoformat()

print('<?xml version="1.0" encoding="UTF-8"?>')
print('<kml xmlns="http://www.opengis.net/kml/2.2">')
print(f"<!-- {today} -->")
print("<Document>")
print(f"<name>{brand.capitalize()}</name>")

if "data" in shops: # Rossmann packs data this way
  shops = shops["data"]
elif "Elements" in shops: # Moya packs data this way
  shops = shops["Elements"]


for shop in shops:
  entry = unpack_shop(shop)
  if entry is None:
    continue

  (lat, lon, label) = entry

  print("<Placemark>")
  print(f"<name>{label}</name>")
  print("<Point>")
  print("<coordinates>")
  print(f"{lon},{lat}")
  print("</coordinates>")
  print("</Point>")
  print("</Placemark>")

print("</Document>")
print("</kml>")

