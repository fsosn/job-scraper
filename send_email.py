import smtplib
from config import APP_EMAIL, PASSWORD, MY_EMAIL
from pretty_html_table import build_table
import pandas as pd


def send_email(report: pd.DataFrame):
    html_report = build_table(report, "blue_light")

    subject = "Job Report"
    message = f"Subject: {subject}\nContent-Type: text/html\n\n{html_report}".encode(
        "utf-8"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=APP_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=APP_EMAIL, to_addrs=MY_EMAIL, msg=message)
