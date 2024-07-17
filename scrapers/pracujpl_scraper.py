import pandas as pd
from .utils.scraper_utils import get_search_criteria_data, get_soup


def scrape():
    url = _build_url()
    soup = get_soup(url)
    job_tiles = soup.find_all("div", class_="tiles_b131b74u")
    job_dict_list = [_extract_job_details(tile) for tile in job_tiles]

    return pd.DataFrame(job_dict_list)


def _build_url():
    job_title, location = get_search_criteria_data()
    return f"https://it.pracuj.pl/praca/{job_title};kw/{location};wp/ostatnich%2024h;p,1?rd=0&et=17%2C1%2C3&sc=0"


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
