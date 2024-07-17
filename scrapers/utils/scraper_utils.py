import requests
import json
from bs4 import BeautifulSoup


def get_soup(url: str):
    page = _fetch_job_page(url)
    return BeautifulSoup(page, "lxml")


def _fetch_job_page(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def get_search_criteria_data():
    with open("search_criteria.json", "r") as file:
        data = json.load(file)

    search_criteria = data["search_criteria"][0]
    job_title = search_criteria["job_title"].lower()
    location = search_criteria["location"].lower()

    return job_title, location
