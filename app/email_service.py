import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from datetime import datetime
import pytz
import base64

from app.config import (
    SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD,
    FROM_EMAIL, TO_EMAIL
)

def send_notification_marketing_email(data):
    subject = "New Demo Request Submitted"

    now_utc = datetime.now(pytz.UTC)
    formatted_time = now_utc.strftime("%A, %d %B %Y %H:%M:%S (UTC)")
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    logo_base64 = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_data = f.read()
            logo_base64 = base64.b64encode(logo_data).decode("utf-8")

    html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#ffffff;">
            <table
                width="100%"
                cellpadding="0"
                cellspacing="0"
                style="font-family: Arial, sans-serif; font-size:14px; color:#333;"
            >
                <tr>
                    <td align="center">

                        <table
                            width="600"
                            cellpadding="10"
                            cellspacing="0"
                            style="max-width:600px; width:100%;"
                        >

                            <!-- Logo (Left aligned, 50% smaller) -->
                            <tr>
                                <td align="left">
                                    {
                                        f"<img src='data:image/png;base64,{logo_base64}' "
                                        "style='max-width:60px; width:60px; height:auto; "
                                        "display:block; margin-bottom:10px;' "
                                        "alt='UBX Cloud'/>"
                                        if logo_base64 else ""
                                    }
                                </td>
                            </tr>

                            <!-- Greeting -->
                            <tr>
                                <td>
                                    <p><b>Hi Marketing Team,</b></p>
                                    <p>
                                        A new Request Demo has been submitted on the website.
                                        Please find the details below and follow up accordingly.
                                    </p>
                                </td>
                            </tr>

                            <!-- Lead Details -->
                            <tr>
                                <td>
                                    <p>
                                        <b>Lead Details</b><br>
                                        First Name: {data.first_name}<br>
                                        Last Name: {data.last_name}<br>
                                        Email: {data.email}<br>
                                        Phone: {data.phone}
                                    </p>
                                </td>
                            </tr>

                            <!-- Requested Information -->
                            <tr>
                                <td>
                                    <p>
                                        <b>Requested Information</b><br>
                                        Nature of Enquiry: {data.nature_of_enquiry}<br>
                                        Looking For: {data.looking_for}
                                    </p>
                                </td>
                            </tr>

                            <!-- Submitted On -->
                            <tr>
                                <td>
                                    <p>
                                        <b>Submitted On</b><br>
                                        {formatted_time}
                                    </p>
                                </td>
                            </tr>

                            <!-- Source -->
                            <tr>
                                <td>
                                    <p>
                                        <b>Source</b><br>
                                        Website – Requested Demo Form
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td>
                                    <p>
                                        Please assign this lead to the appropriate owner and
                                        initiate the next steps as per the lead handling process.
                                    </p>
                                    <p>
                                        <br>
                                        Thanks,<br>
                                        Website Automation System
                                    </p>
                                </td>
                            </tr>

                        </table>

                    </td>
                </tr>
            </table>
        </body>
        </html>
        """


    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())


def send_notification_customer_email(data):
    subject = "Thanks for   Requesting a Demo - We'll Be in Touch"

    now_utc = datetime.now(pytz.UTC)
    formatted_time = now_utc.strftime("%A, %d %B %Y %H:%M:%S (UTC)")
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    logo_base64 = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_data = f.read()
            logo_base64 = base64.b64encode(logo_data).decode("utf-8")

    html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#ffffff;">
            <table
                width="100%"
                cellpadding="0"
                cellspacing="0"
                style="font-family: Arial, sans-serif; font-size:14px; color:#333;"
            >
                <tr>
                    <td align="center">

                        <table
                            width="600"
                            cellpadding="10"
                            cellspacing="0"
                            style="max-width:600px; width:100%;"
                        >

                            <!-- Logo (Left aligned, 50% smaller) -->
                            <tr>
                                <td align="left">
                                    {
                                        f"<img src='data:image/png;base64,{logo_base64}' "
                                        "style='max-width:60px; width:60px; height:auto; "
                                        "display:block; margin-bottom:10px;' "
                                        "alt='UBX Cloud'/>"
                                        if logo_base64 else ""
                                    }
                                </td>
                            </tr>

                            <!-- Greeting -->
                            <tr>
                                <td>
                                    <p><b>Hi {data.first_name} {data.last_name},</b></p><br>
                                    <p>
                                        Thank you for reaching out to us!👋<br>
                                        We've received your demo request, and our team is reviewing the details.
                                    </p>
                                </td>
                            </tr>

                            <!-- Here's A Quick Summary Of Your Request: -->
                            <tr>
                                <td>
                                    <p>
                                        <b>Here's A Quick Summary Of Your Request:</b><br><br>
                                        Nature of Enquiry: {data.nature_of_enquiry}<br>
                                        Looking For: {data.looking_for}
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td>
                                    <p>
                                        One of specialists will contact you shortly to understand 
                                        your requirment and schedule the demo at a convenient time.
                                    </p>
                                </td>
                            </tr>

                            <tr>
                                <td>
                                    <p>
                                        If you have any additional information to share, feel free to reply to this email.<br>
                                        Looking forward to connecting with you.
                                    </p>
                                    <p>
                                        <br>
                                        Thanks,<br>
                                        Marketing Team<br>
                                        UBX Cloud
                                    </p>
                                </td>
                            </tr>

                        </table>

                    </td>
                </tr>
            </table>
        </body>
        </html>
        """

    TO_EMAIL = data.email
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())


def send_email_with_pdf(data, pdf_path):
    subject = "Configuration Summary"

    html_body = """
    <html>
    <body>
        <p>Please find the configuration summary attached.</p>
        <p>Thank you.</p>
    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    msg.attach(MIMEText(html_body, "html"))

    # Attach PDF
    with open(pdf_path, "rb") as f:
        pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
        pdf_attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename=os.path.basename(pdf_path)
        )
        msg.attach(pdf_attachment)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
