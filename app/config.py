from dotenv import load_dotenv
import os

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
PHONE = os.getenv("PHONE")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL")
