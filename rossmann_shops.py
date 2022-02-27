#!/usr/bin/python3

import json
import sys
from datetime import date

shops = json.load(sys.stdin)["data"]

today = date.today().isoformat()

print('<?xml version="1.0" encoding="UTF-8"?>')
print('<kml xmlns="http://www.opengis.net/kml/2.2">')
print(f"<!-- {today} -->")
print("<Document>")
print("<name>Rossmann</name>")

for shop in shops:
  coords = shop["shopLocation"]
  lat = coords["latitude"]
  lon = coords["longitude"]
  addr = shop["address"]
  label = f"{addr['city']}, {addr['street']}"

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

