"""Helper functions for the project"""

from bs4 import BeautifulSoup, Tag
import requests


def get_document(link: str) -> BeautifulSoup:
    """
    Gets the document of the page

    :param link: The link to the page

    :return: The document of the page as a BeautifulSoup object
    """

    response = requests.get(
        url=link,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        timeout=10,
    )

    return BeautifulSoup(response.text, "lxml")


def next_page_link(document: BeautifulSoup | Tag) -> str | None:
    """
    Extracts the link to the next page

    :param document: The document containing the page

    :return: The link to the next page
    """

    next_page = document.find(
        "a", attrs={"class": "prevnextbutton", "title": "Next page"}
    )

    if next_page is None:
        return None
    return "https://www.gsmarena.com/" + next_page.get("href", None)
