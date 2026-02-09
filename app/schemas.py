from pydantic import BaseModel, EmailStr
from typing import List

class EmailRequest(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    nature_of_enquiry: str
    looking_for: str


class ConfigurationItem(BaseModel):
    name: str
    quantity: str
    price: str

class PdfEmailRequest(BaseModel):
    selected_configuration: List[ConfigurationItem]
    total_cost: str