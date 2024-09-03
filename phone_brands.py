"""A script to extract the phone brands in csv format from the GSM Arena website."""

import csv
from inspect import getsourcefile
from os.path import abspath, dirname, join

import requests
from bs4 import BeautifulSoup, Tag

from utils.classes import Brand


print("Extracting phone brands from GSM Arena...")


# Get the directory path of the current file
current_dir = dirname(abspath(getsourcefile(lambda: 0)))


response = requests.get(
    url="https://www.gsmarena.com/makers.php3",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    },
    timeout=10,
)

# Parsing the response
document = BeautifulSoup(response.text, "lxml")
# Extracting the table containing the phone brands
table = document.find("div", class_="st-text").find("table")


# Extracting the phone brands and writing them to a CSV file
with open(
    join(current_dir, "data", "phone_brands.csv"), "w", newline="", encoding="utf-8"
) as file:
    writer = csv.DictWriter(file, ["id", "name", "number_of_devices", "gsmarena_link"])
    writer.writeheader()

    td: Tag  # Used to specify the type of the variable for type hinting
    for td in table.find_all("td"):
        td_a = td.find("a")
        td_span = td.find("span")
        brand = Brand(
            id=td_a.get("href").split(".")[0],
            # stripped_strings is a generator and next() returns the next item in the generator
            name=next(td_a.stripped_strings),
            number_of_devices=int(td_span.text.split(" ")[0]),
            gsmarena_link="https://www.gsmarena.com/" + td_a.get("href"),
        )
        writer.writerow(brand.__dict__)


print("Phone brands extracted successfully.")
