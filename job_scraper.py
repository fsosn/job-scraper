from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import logging
import sys

logging.basicConfig(
    filename="job_scraping.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def scrape_pracujpl():
    url = _build_url()

    try:
        job_page = _fetch_job_page(url)
    except requests.HTTPError as e:
        logging.error(f"Failed to fetch job page from {url}: {e}")
        sys.exit(1)

    soup = BeautifulSoup(job_page, "lxml")

    job_tiles = soup.find_all("div", class_="tiles_b131b74u")

    job_dict_list = [_extract_job_details(tile) for tile in job_tiles]

    return pd.DataFrame(job_dict_list)


def _build_url():
    with open("search_criteria.json", "r") as file:
        data = json.load(file)

    search_criteria = data["search_criteria"][0]
    job_title = search_criteria["job_title"].lower()
    location = search_criteria["location"].lower()

    return f"https://it.pracuj.pl/praca/{job_title};kw/{location};wp/ostatnich%2024h;p,1?rd=0&et=17%2C1%2C3&sc=0"


def _fetch_job_page(url: str):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def _extract_job_details(tile):
    h2 = tile.find("h2")
    job_title, job_href = None, None
    if h2:
        tag = h2.find("a")
        if tag:
            job_title = tag.get_text(strip=True)
            job_href = tag.get("href")
        else:
            job_title = h2.getText()

    job_company = tile.find(
        "h3", class_="tiles_c1rl4c7t size-caption core_t1rst47b"
    ).get_text()

    return {"title": job_title, "company": job_company, "link": job_href}
