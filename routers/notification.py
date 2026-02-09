from fastapi import APIRouter, HTTPException
from app.schemas import EmailRequest
from app.email_service import send_notification_marketing_email, send_notification_customer_email
from app.schemas import PdfEmailRequest
from app.pdf_service import generate_pdf
from app.email_service import send_email_with_pdf
import os
import tempfile
from datetime import datetime

router = APIRouter()

@router.post("/request/marketing/email")
def send_email(payload: EmailRequest):
    try:
        send_notification_marketing_email(payload)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/request/customer/email")
def send_email(payload: EmailRequest):
    try:
        send_notification_customer_email(payload)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/summary/email-with-pdf")
def send_email_pdf(payload: PdfEmailRequest):
    try:
        today = datetime.now().strftime("%d_%m_%Y")
        filename = f"ubx_cloud_{today}.pdf"

        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, filename)

        generate_pdf(payload, file_path)
        send_email_with_pdf(payload, file_path)

        os.remove(file_path)

        return {"message": "Email with PDF sent successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
def health_check():
    return {"status": "running"}