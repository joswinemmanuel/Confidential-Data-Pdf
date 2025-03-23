from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import string
import os

def generate_fake_data(num_entries=20):
    """Generates fake confidential data."""
    data = []
    for _ in range(num_entries):
        website = ''.join(random.choice(string.ascii_lowercase) for i in range(8)) + ".com"
        username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
        password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()") for i in range(16))
        data.append((website, username, password))
    return data

def create_pdf(filename="confidential_data.pdf", data=None):
    """Creates a PDF with the given data."""
    if data is None:
        data = generate_fake_data()

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)
    y = height - 50
    c.drawString(50, y, "Confidential Data")
    y -= 20
    c.line(50, y, width - 50, y)  # Horizontal line
    y -= 20

    for website, username, password in data:
        c.drawString(50, y, f"Website: {website}")
        y -= 15
        c.drawString(50, y, f"Username: {username}")
        y -= 15
        c.drawString(50, y, f"Password: {password}")
        y -= 25
        if y < 50:
            c.showPage()  # Start a new page
            y = height - 50
            c.setFont("Helvetica", 12)
            c.drawString(50, y, "Confidential Data (Continued)")
            y -= 20
            c.line(50, y, width - 50, y)
            y -= 20

    c.save()

def check_pdf_size(filename):
    """Checks the size of the generated PDF."""
    file_size = os.path.getsize(filename)
    print(f"PDF size: {file_size} bytes")
    if file_size <= 500 * 1024: #check under 500kb
        print("PDF size is within the limit.")
        return True
    else:
        print("PDF size exceeds the limit.")
        return False

# Generate and save the PDF
create_pdf()
check_pdf_size("confidential_data.pdf")