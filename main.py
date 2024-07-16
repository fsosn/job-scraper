from job_scraper import scrape_pracujpl
from send_email import send_email


if __name__ == "__main__":
    job_df = scrape_pracujpl()
    send_email(job_df)
