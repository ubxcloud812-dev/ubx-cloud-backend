from pydantic import BaseModel, EmailStr
from typing import List, Optional

class EmailRequest(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    nature_of_enquiry: Optional[str] = None
    looking_for: Optional[str] = None


class ConfigurationItem(BaseModel):
    name: str
    quantity: str
    price: str

class PdfEmailRequest(BaseModel):
    selected_configuration: List[ConfigurationItem]
    total_cost: str
    customer_info: EmailRequest