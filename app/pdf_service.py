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
    elements = []

    # ---------- Logo ----------
    logo_path = os.path.join("assets", "Logo_UBXCloud-1.png")
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=1.5 * inch, height=0.5 * inch)
        logo.hAlign = "CENTER"
        elements.append(logo)
        elements.append(Spacer(1, 20))

    # ---------- Title ----------
    elements.append(
        Paragraph("<b>Configure & Estimate – View Summary</b>", styles["Title"])
    )
    elements.append(Spacer(1, 20))

    # ---------- Table Data ----------
    table_data = [
        ["Selected Configuration", "Quantity", "Price"]
    ]

    for item in data.selected_configuration:
        table_data.append([
            item.name,
            str(item.quantity),
            f"{item.price}"
        ])

    # Separator row (empty content, just line)
    table_data.append(["", "", ""])

    # Total Cost row
    table_data.append([
        "Total Cost",
        "",
        f"{data.total_cost}"
    ])

    # ---------- Table ----------
    table = Table(
        table_data,
        colWidths=[300, 90, 90]
    )

    table.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
        ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),

        # Body alignment
        ("ALIGN", (0, 1), (0, -2), "LEFT"),
        ("ALIGN", (1, 1), (1, -2), "LEFT"),
        ("ALIGN", (2, 1), (2, -2), "LEFT"),
        ("LEFTPADDING", (1, 1), (2, -2), 5),

        # Reduce bottom padding of last item row (second line will move up)
        ("BOTTOMPADDING", (0, -2), (-1, -2), 2),  # smaller bottom padding
        ("TOPPADDING", (0, -2), (-1, -2), 4),     # optional, smaller top padding

        # Line after last item (second line)
        ("LINEBELOW", (0, -2), (-1, -2), 1, colors.black),

        # Total row emphasis
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("LINEBELOW", (0, -1), (-1, -1), 1, colors.black),

        # General padding for other rows
        ("TOPPADDING", (0, 1), (-1, -3), 8),
        ("BOTTOMPADDING", (0, 1), (-1, -3), 8),
    ]))


    elements.append(table)
    doc.build(elements)
