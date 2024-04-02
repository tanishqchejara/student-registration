
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf(name, aicte_id, email, phone, college):
    pdf_filename = f"{name}_registration.pdf"

    # Create PDF document
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()

    # Define custom styles
    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        textColor=colors.blue,
        fontSize=18,
        alignment=1,
        spaceAfter=20
    )

    normal_style = ParagraphStyle(
        "Normal",
        parent=styles["Normal"],
        fontSize=12,
        spaceAfter=10
    )

    # Add data to PDF
    content = []

    # Title
    title_text = "<u>Student Registration Form</u>"
    content.append(Paragraph(title_text, title_style))
    content.append(Spacer(1, 20))  # Add space

    # Information
    info_text = f"<br/><br/><b>Name:</b>{name}<br/><br/><b>AICTE ID:</b> {aicte_id}<br/><br/><b>Email:</b> {email}<br/><br/>" \
                f"<b>Phone:</b> {phone}<br/><br/><b>College:</b> {college}"
    content.append(Paragraph(info_text, normal_style))

    doc.build(content)
