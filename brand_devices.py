"""Stores the devices of a brand in csv format from gsmarena's brand page."""

import csv
from inspect import getsourcefile
from os.path import abspath, dirname, join

from utils.scraper import get_brand_devices_generator, get_brands_generator

# Get the directory path of this file
current_dir = dirname(abspath(getsourcefile(lambda: 0)))


print("-------------------------------------------------------------")
print("Started extracting devices of phone brands from GSM Arena...")
print("-------------------------------------------------------------")
for brand in get_brands_generator():
    print("-------------------------------------------------------------")
    print(f"Extracting devices of {brand.name}...")

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

        for device in get_brand_devices_generator(brand.gsmarena_link, 3000):
            writer.writerow(device.__dict__)
    print(f"Devices of {brand.name} extracted successfully.")
    print("-------------------------------------------------------------")

print("-------------------------------------------------------------")
print("Devices of all phone brands extracted successfully.")
print("-------------------------------------------------------------")
