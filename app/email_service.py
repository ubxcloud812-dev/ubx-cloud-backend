import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from datetime import datetime
import pytz
import base64

from app.config import (
    SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD,
    FROM_EMAIL, TO_EMAIL, SUPPORT_EMAIL, PHONE
)

def send_notification_marketing_email(data):
    subject = "New Demo Request Received from Website"

    now_utc = datetime.now(pytz.UTC)
    formatted_time = now_utc.strftime("%A, %d %B %Y %H:%M:%S (UTC)")
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#ffffff;">
            <table width="100%" cellpadding="0" cellspacing="0"
                style="font-family: Arial, sans-serif; font-size:14px; color:#333;">
                <tr>
                    <td align="center">

                        <table width="600" cellpadding="10" cellspacing="0"
                            style="max-width:600px; width:100%;">

                            <!-- Logo -->
                            <tr>
                                <td align="left">
                                    <img src="cid:ubx_logo"
                                        alt="UBX Cloud"
                                        style="max-width:80px; height:auto; display:block; margin:0 0 20px 0;">
                                </td>
                            </tr>

                            <!-- Greeting -->
                            <tr>
                                <td>
                                    <p><b>Hi Marketing Team,</b></p>
                                    <p>
                                        A new Request Demo submission has been received through the website.  
                                        Please review the details below and follow up with the customer accordingly.
                                    </p>
                                </td>
                            </tr>

                            <!-- Lead Details -->
                            <tr>
                                <td>
                                    <p style="margin:0 0 8px 0;"><b>Lead Details</b></p>
                                    <dl style="margin:0; padding:0;">
                                        <dt><b>First Name: </b>{data.first_name}</dt>

                                        <dt><b>Last Name: </b>{data.last_name}</dt>

                                        <dt><b>Email: </b>{data.email}</dt>

                                        <dt><b>Phone: </b>{data.phone}</dt>
                                    </dl>
                                </td>
                            </tr>

                            <!-- Requested Information -->
                            <tr>
                                <td>
                                    <p style="margin:16px 0 8px 0;"><b>Requested Information</b></p>
                                    <dl style="margin:0; padding:0;">
                                        <dt><b>Nature of Enquiry: </b>{data.nature_of_enquiry}</dt>

                                        <dt><b>Looking For: </b>{data.looking_for}</dt>
                                    </dl>
                                </td>
                            </tr>

                            <!-- Submission Details -->
                            <tr>
                                <td>
                                    <p style="margin:0 0 6px 0;"><b>Submission Details</b></p>

                                    <p style="margin:0;">
                                        <b>Submitted On:</b> {formatted_time}
                                    </p>

                                    <p style="margin:0;">
                                        <b>Source:</b> Website – Requested Demo Form
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td>
                                    <p style="margin:16px 0 0 0;">
                                        Please assign this lead to the appropriate owner and initiate the next steps,  
                                        including demo scheduling or a consultation, as per the lead handling process.
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

    with open(logo_path, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "<ubx_logo>")
        img.add_header("Content-Disposition", "inline", filename="Logo_UBXCloud-1.png")
        msg.attach(img)
    
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())


def send_notification_customer_email(data):
    subject = "Thanks for Requesting a Demo - We'll Be in Touch"

    now_utc = datetime.now(pytz.UTC)
    formatted_time = now_utc.strftime("%A, %d %B %Y %H:%M:%S (UTC)")
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    TO_EMAIL = data.email
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#ffffff;">
            <table width="100%" cellpadding="0" cellspacing="0"
                style="font-family: Arial, sans-serif; font-size:14px; color:#333;">
                <tr>
                    <td align="center">

                        <table width="600" cellpadding="10" cellspacing="0"
                            style="max-width:600px; width:100%;">

                            <!-- Logo -->
                            <img src="cid:ubx_logo"
                                alt="UBX Cloud"
                                style="
                                    max-width:80px;
                                    height:auto;
                                    display:block;
                                    margin:0 0 20px 0;
                                ">

                            <!-- Greeting -->
                            <tr>
                                <td>
                                    <p style="margin:0 0 6px 0;">
                                        <b>Hi {data.first_name} {data.last_name},</b>
                                    </p>
                                    <p style="margin:0;">
                                        We’ve received your demo request, and our team is currently reviewing the details you shared. Below is a 
                                        quick summary of your request for your reference:
                                    </p>
                                </td>
                            </tr>

                            <!-- Request Summary -->
                            <tr>
                                <td>
                                    <p style="margin:16px 0 6px 0;">
                                        <b>Request Summary</b>
                                    </p>

                                    <dl style="margin:0; padding:0;">
                                        <dt><b>Nature of Enquiry: </b>{data.nature_of_enquiry}</dt>

                                        <dt><b>Looking For: </b>{data.looking_for}</dt>
                                    </dl>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td>
                                    <p style="margin:16px 0 0 0;">
                                        One of our specialists will contact you shortly to better understand  
                                        your requirements and schedule a demo at a time that’s convenient for you.
                                    </p>
                                </td>
                            </tr>

                            <tr>
                                <td>
                                    <p style="margin:12px 0 0 0;">
                                        If you have any additional information to share or updates to your request, 
                                        feel free to reply to this email. We look forward to connecting with you.
                                    </p>
                                    <p style="margin:12px 0 0 0;">
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


    with open(logo_path, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "<ubx_logo>")
        img.add_header("Content-Disposition", "inline", filename="Logo_UBXCloud-1.png")
        msg.attach(img)
    
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())


def send_email_with_pdf(data, pdf_path):
    subject = "Your Cloud Cost Estimation Summary"

    now_utc = datetime.now(pytz.UTC)
    formatted_time = now_utc.strftime("%A, %d %B %Y %H:%M:%S (UTC)")
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject

    html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#ffffff;">
            <div style="
                font-family: Arial, sans-serif;
                font-size:14px;
                color:#333;
                max-width:600px;
                margin:0 auto;
                padding:24px;
            ">

                <!-- Logo -->
                <img src="cid:ubx_logo"
                    alt="UBX Cloud"
                    style="
                        max-width:80px;
                        height:auto;
                        display:block;
                        margin:0 0 20px 0;
                    ">

                <!-- Greeting -->
                <p style="margin:0 0 12px 0;">
                    <b>Hi {data.customer_info.first_name} {data.customer_info.last_name},</b>
                </p>

                <p style="margin:0 0 12px 0;">
                    Thank you for reaching out to us! 👋<br><br>
                    Based on the configuration you selected, we’ve generated a detailed cost estimation for your cloud 
                    requirements. Please find the attached PDF, which outlines the estimated pricing and related details.
                </p>

                <!-- Contact Info -->
                <p style="margin:20px 0 8px 0;">
                    If you need any adjustments, have additional requirements, or would like to discuss this estimate further, 
                    feel free to reach out to us using the contact information below.
                </p>

                <p style="margin:0;">
                    <b>Email:</b> {SUPPORT_EMAIL}<br>
                    <b>Phone:</b> {PHONE}
                </p>

                <!-- Footer note -->
                <p style="margin:20px 0 0 0; color:#666;">
                    This is an auto-generated email. Please do not reply directly to this message.
                </p>

            </div>
        </body>
        </html>
        """



    with open(logo_path, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "<ubx_logo>")
        img.add_header("Content-Disposition", "inline", filename="Logo_UBXCloud-1.png")
        msg.attach(img)

    msg.attach(MIMEText(html_body, "html"))

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


def send_customer_summary_email(data):
    subject = "New Configure & Cost Estimate Sent to Customer"

    now_utc = datetime.now(pytz.UTC)
    formatted_time = now_utc.strftime("%A, %d %B %Y %H:%M:%S (UTC)")
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")

    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    
    config_rows = ""

    for item in data.selected_configuration:
        config_rows += f"""
            <tr>
                <td style="padding:4px 0;">
                    <b>{item.name}</b>: {item.quantity} = {item.price}
                </td>
            </tr>
        """

    html_body = f"""
        <html>
        <body style="margin:0; padding:0; background-color:#ffffff;">
            <table width="100%" cellpadding="0" cellspacing="0"
                style="font-family: Arial, sans-serif; font-size:14px; color:#333;">
                <tr>
                    <td align="center">

                        <table width="600" cellpadding="0" cellspacing="0"
                            style="max-width:600px; width:100%; padding:24px;">

                            <!-- Logo -->
                            <tr>
                                <td align="left">
                                    <img src="cid:ubx_logo"
                                        alt="UBX Cloud"
                                        style="max-width:60px; height:auto; display:block; margin-bottom:20px;">
                                </td>
                            </tr>

                            <!-- Greeting -->
                            <tr>
                                <td>
                                    <p style="margin:0 0 12px 0;">
                                        <b>Hi Marketing Team,</b>
                                    </p>
                                    <p style="margin:0 0 20px 0;">
                                        A cloud configuration and cost estimation has been successfully generated and sent to a customer.
                                        Please find the lead and configuration details below and proceed with the next steps as per the lead follow-up process.
                                    </p>
                                </td>
                            </tr>

                            <!-- Lead Details -->
                            <tr>
                                <td>
                                    <p style="margin:0 0 8px 0;"><b>Lead Details:</b></p>

                                    <dl style="margin:0; padding:0;">
                                        <dt><b>First Name:</b> {data.customer_info.first_name}</dt>

                                        <dt><b>Last Name:</b> {data.customer_info.last_name}</dt>

                                        <dt><b>Email:</b> {data.customer_info.email}</dt>

                                        <dt><b>Phone:</b> {data.customer_info.phone}</dt>
                                    </dl>
                                </td>
                            </tr>

                            <!-- Configure & Estimate Details -->
                            <tr>
                                <td style="padding-top:20px;">
                                    <p style="margin:0 0 8px 0;"><b>Configure & Estimate Details:</b></p>

                                    <dl style="margin:0; padding:0;">
                                        {config_rows}
                                    </dl>

                                    <p style="margin:12px 0 0 0;">
                                        <b>Total Cost:</b> {data.total_cost}
                                    </p>
                                </td>
                            </tr>

                            <!-- Submitted On -->
                            <tr>
                                <td style="padding-top:20px;">
                                    <p style="margin:0;">
                                        <b>Submitted On</b><br>
                                        {formatted_time}
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td style="padding-top:20px;">
                                    <p style="margin:0 0 12px 0;">
                                        Kindly assign this lead to the appropriate owner and initiate follow-up actions, including demo scheduling or 
                                        consultation if required
                                    </p>
                                    <p style="margin:0;">
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


    with open(logo_path, "rb") as f:
        img = MIMEImage(f.read())
        img.add_header("Content-ID", "<ubx_logo>")
        img.add_header("Content-Disposition", "inline", filename="Logo_UBXCloud-1.png")
        msg.attach(img)
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
