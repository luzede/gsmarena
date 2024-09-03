"""Functions that scrape the data from the gsmarena website"""

from collections.abc import Iterator
import random
import time
from typing import List

from bs4 import Tag

from utils.classes import Device, DeviceDetails, DeviceSpecs, Brand
from utils.helper import get_document, next_page_link
from utils.extractor import device_details, device_specs


def get_brand_devices(link: str, rand_delay_max: int = 0) -> List[Device]:
    """
    Extracts brand devices from the page

    :param link: The link to the phone's page

    :param rand_delay_max: The maximum value of the random delay in ms before sending the requests

    :return: A dictionary containing the phone data
    """
    devices: List[Device] = []
    link: str | None

    while link is not None:
        if int(rand_delay_max) > 0:
            time.sleep(random.randint(1, rand_delay_max) / 1000)

        document = get_document(link)

        section_body = document.find(
            "div", attrs={"class": "section-body", "id": "review-body"}
        )

        for a in section_body.find_all("a"):
            img: Tag = a.find("img")
            name: Tag = a.find("strong")

            devices.append(
                Device(
                    title=name.text,
                    extended_title=img.get("title"),
                    img_link=img.get("src"),
                    gsmarena_link=a.get("href"),
                )
            )

        link = next_page_link(document)

    return devices


def get_brand_devices_generator(link: str, rand_delay_max: int = 0) -> Iterator[Device]:
    """
    Extracts brand devices from gsmarena,

    :param link: The link to the brand's page on gsmarena

    :param rand_delay_max: The maximum value of the random delay in ms before sending the requests

    :return: A generator that yields **Device** dataclass objects
    """
    link: str | None

    while link is not None:
        if int(rand_delay_max) > 0:
            time.sleep(random.randint(1, rand_delay_max) / 1000)

        document = get_document(link)

        section_body = document.find(
            "div", attrs={"class": "section-body", "id": "review-body"}
        )

        for a in section_body.find_all("a"):
            img: Tag = a.find("img")
            name: Tag = a.find("strong")

            yield Device(
                title=name.text,
                extended_title=img.get("title"),
                img_link=img.get("src"),
                gsmarena_link="https://www.gsmarena.com/" + a.get("href"),
            )

        link = next_page_link(document)


def get_device_details(link: str) -> DeviceDetails:
    """
    Extracts the device details from the page

    :param link: The link to the device's page

    :return: A dictionary containing the device data
    """

    document = get_document(link)

    # Extracting the data
    return device_details(document)


def get_device_specs(link: str) -> DeviceSpecs:
    """
    Extracts the device specs from the page

    :param link: The link to the device's page

    :return: A dictionary containing the device specs
    """

    document = get_document(link)

    # Extracting the data
    return device_specs(document)


def get_brands() -> List[Brand]:
    """
    Extracts the brands from the page

    :return: A list of brands
    """

    document = get_document("https://www.gsmarena.com/makers.php3")

    table = document.find("div", class_="st-text").find("table")

    brands: List[Brand] = []

    td: Tag
    for td in table.find_all("td"):
        td_a = td.find("a")
        td_span = td.find("span")
        brand = Brand(
            id=td_a.get("href").split(".")[0],
            name=next(td_a.stripped_strings),
            number_of_devices=int(td_span.text.split(" ")[0]),
            gsmarena_link="https://www.gsmarena.com/" + td_a.get("href"),
        )
        brands.append(brand)

    return brands


def get_brands_generator() -> Iterator[Brand]:
    """
    Extracts the brands from the page

    :return: A generator that yields **Brand** dataclass objects
    """

    document = get_document("https://www.gsmarena.com/makers.php3")

    table = document.find("div", class_="st-text").find("table")

    td: Tag
    for td in table.find_all("td"):
        td_a = td.find("a")
        td_span = td.find("span")
        brand = Brand(
            id=td_a.get("href").split(".")[0],
            name=next(td_a.stripped_strings),
            number_of_devices=int(td_span.text.split(" ")[0]),
            gsmarena_link="https://www.gsmarena.com/" + td_a.get("href"),
        )
        yield brand
