from selenium import webdriver
from selenium.webdriver.common.by import By
from .utils.scraper_utils import get_search_criteria_data
import pandas as pd


def scrape():
    url = _build_url()
    driver = _setup_driver()
    driver.get(url)
    job_posting_elements = driver.find_elements(
        By.CSS_SELECTOR, value="td.resultContent"
    )
    job_dict_list = [
        _extract_title_and_company(element) for element in job_posting_elements
    ]
    driver.quit()
    return pd.DataFrame(job_dict_list)


def _extract_title_and_company(job_posting_element):
    job_href = job_posting_element.find_element(
        By.CSS_SELECTOR, value="a"
    ).get_attribute("href")
    spans = job_posting_element.find_elements(By.CSS_SELECTOR, value="span")
    job_title, job_company = spans[0].text, spans[1].text
    return {"title": job_title, "company": job_company, "link": job_href}


def _setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    return driver


def _build_url():
    job_title, location = get_search_criteria_data()
    return f"https://pl.indeed.com/jobs?q={job_title}&l={location}&sort=date&fromage=1"
