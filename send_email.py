import smtplib
from config import FROM_EMAIL, PASSWORD, TO_EMAIL
from pretty_html_table import build_table
import pandas as pd


def send_email(*reports: pd.DataFrame):
    html_report = ""
    for report in reports:
        html_report += build_table(report, "blue_light")

    subject = "Job Report"
    message = f"Subject: {subject}\nContent-Type: text/html\n\n{html_report}".encode(
        "utf-8"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=message)
