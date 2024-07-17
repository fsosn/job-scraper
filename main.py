from scrapers import pracujpl_scraper
from send_email import send_email
import logging
import sys

logging.basicConfig(
    filename="job_scraping.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    logging.info("Starting job scraping.")
    try:
        job_df = pracujpl_scraper.scrape()
        logging.info("Job scraping completed.")
        send_email(job_df)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
