from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Spacer,
    Image,
    Paragraph
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors
import os


def generate_pdf(data, file_path: str):
    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    elements = []

    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=1.5 * inch, height=0.5 * inch)
        logo.hAlign = "CENTER"
        elements.append(logo)
        elements.append(Spacer(1, 20))

    elements.append(
        Paragraph("<b>Configure & Estimate – View Summary</b>", styles["Title"])
    )
    elements.append(Spacer(1, 20))

    table_data = [[
        Paragraph("<b>Selected Configuration</b>", normal_style),
        Paragraph("<b>Quantity</b>", normal_style),
        Paragraph("<b>Price</b>", normal_style)
    ]]

    for item in data.selected_configuration:
        table_data.append([
            Paragraph(item.name, normal_style),
            Paragraph(str(item.quantity), normal_style),
            Paragraph(f"{item.price}", normal_style)
        ])
    
    table_data.append(["", "", ""])

    table_data.append([
        "Total Cost",
        "",
        f"{data.total_cost}"
    ])

    table = Table(
        table_data,
        colWidths=[300, 90, 90]
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),
        ("ALIGN", (0, 1), (0, -2), "LEFT"),
        ("ALIGN", (1, 1), (1, -2), "LEFT"),
        ("ALIGN", (2, 1), (2, -2), "LEFT"),
        ("LEFTPADDING", (1, 1), (2, -2), 5),
        ("BOTTOMPADDING", (0, -2), (-1, -2), 2),
        ("TOPPADDING", (0, -2), (-1, -2), 4),
        ("LINEBELOW", (0, -2), (-1, -2), 1, colors.black),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("LINEBELOW", (0, -1), (-1, -1), 1, colors.black),
        ("TOPPADDING", (0, 1), (-1, -3), 8),
        ("BOTTOMPADDING", (0, 1), (-1, -3), 8),
    ]))


    elements.append(table)
    elements.append(Spacer(1, 30))

    elements.append(
        Paragraph("<b>Customer Information</b>", styles["Heading2"])
    )
    elements.append(Spacer(1, 10))

    customer = data.customer_info

    customer_table_data = [
        ["First Name", customer.first_name],
        ["Last Name", customer.last_name],
        ["Email", customer.email],
        ["Phone", customer.phone],
        ["Nature of Enquiry", customer.nature_of_enquiry],
        ["Looking For", customer.looking_for],
    ]

    customer_table = Table(
        customer_table_data,
        colWidths=[110, 370],
        hAlign="LEFT"
    )

    customer_table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))

    elements.append(customer_table)

    doc.build(elements)

