"""Stores the devices of a brand in csv format from gsmarena's brand page."""

import csv
import json
from inspect import getsourcefile
from os.path import abspath, dirname, join

from utils.scraper import get_brand_devices_generator, get_brands_generator

# Get the directory path of this file
current_dir = dirname(abspath(getsourcefile(lambda: 0)))

brand_devices = {}


print("-------------------------------------------------------------")
print("Started extracting devices of phone brands from GSM Arena...")
print("-------------------------------------------------------------")
for brand in get_brands_generator():
    print("-------------------------------------------------------------")
    print(f"Extracting devices of {brand.name}...")
    brand_devices[brand.id] = {
        "name": brand.name,
        "gsmarena_link": brand.gsmarena_link,
        "number_of_devices": brand.number_of_devices,
        "devices": [],
    }

    with open(
        join(current_dir, "data", "brands", f"{brand.name.lower()}_devices.csv"),
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file, ["title", "extended_title", "img_link", "gsmarena_link"]
        )
        writer.writeheader()

        for device in get_brand_devices_generator(brand.gsmarena_link, 5000):
            writer.writerow(device.__dict__)
            brand_devices[brand.id]["devices"].append(device.__dict__)
    print(f"Devices of {brand.name} extracted successfully.")
    print("-------------------------------------------------------------")


with open(
    join(current_dir, "data", "brand_devices.json"), "w", encoding="utf-8"
) as file:
    json.dump(brand_devices, file, indent=4)

print("-------------------------------------------------------------")
print("Devices of all phone brands extracted successfully.")
print("-------------------------------------------------------------")
