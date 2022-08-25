#!/usr/bin/python3

import json
import sys
from datetime import date
import csv

def csv_load(file):
  rows = []
  csvreader = csv.reader(file)
  for row in csvreader:
    rows.append(row)
  return rows

brand = sys.argv[1]

def unpack_shop(shop):
  if brand=="circlek":
    label = shop[0]
    lat = shop[1]
    lon = shop[2]
  elif brand=="zabka":
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
  elif brand=="lewiatan":
    lat = shop["latitude"]
    lon = shop["longitude"]
    label = f"{shop['city']}, {shop['address']}"
  else:
    raise Exception(f"Unknown brand {brand}")

  return lat, lon, label


today = date.today().isoformat()

if brand=="circlek":
  shops = csv_load(sys.stdin)
else:
    shops = json.load(sys.stdin)

if "data" in shops: # Rossmann and Lewiatan packs data this way
  shops = shops["data"]
elif "Elements" in shops: # Moya packs data this way
  shops = shops["Elements"]

with open(f"{brand.capitalize()}.kml", 'x') as kml_file: # fails if file already exists
  def writeline(s):
    kml_file.write(s)
    kml_file.write("\n")

  writeline('<?xml version="1.0" encoding="UTF-8"?>')
  writeline('<kml xmlns="http://www.opengis.net/kml/2.2">')
  writeline(f"<!-- {today} -->")
  writeline("<Document>")
  writeline(f"<name>{brand.capitalize()}</name>")

  count = 0

  for shop in shops:
    entry = unpack_shop(shop)
    if entry is None:
      continue

    (lat, lon, label) = entry
    label = label.replace("&nbsp;"," ")

    count += 1

    writeline("<Placemark>")
    writeline(f"<name>{label}</name>")
    writeline("<Point>")
    writeline("<coordinates>")
    writeline(f"{lon},{lat}")
    writeline("</coordinates>")
    writeline("</Point>")
    writeline("</Placemark>")

  writeline("</Document>")
  writeline("</kml>")

print(f"Extracted {count} entries.")
