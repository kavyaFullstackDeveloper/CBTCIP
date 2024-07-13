from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_receipt(receipt_info, filename="payment_receipt.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    # Add receipt details
    c.setFont("Helvetica", 12)
    text = f"""
    Date: {receipt_info['date']}
    Receipt Number: {receipt_info['receipt_number']}

    Payer Information:
    Name: {receipt_info['payer_name']}
    Email: {receipt_info['payer_email']}
    Contact: {receipt_info['payer_contact']}

    Payment Details:
    Amount: {receipt_info['amount']}
    Payment Method: {receipt_info['payment_method']}
    """

    # Add lines to the PDF
    lines = text.split("\n")
    y = height - 100
    for line in lines:
        c.drawString(100, y, line.strip())
        y -= 20

    # Add a thank you note
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y - 20, "Thank you for your payment!")

    # Save the PDF
    c.save()

# Example usage
receipt_info = {
    "date": "2024-07-13",
    "receipt_number": "123456789",
    "payer_name": "kavya yadla",
    "payer_email": "kavya.why@example.com",
    "payer_contact": "+91 9876543210",
    "amount": "$111.00",
    "payment_method": "Credit Card 2",
}

create_receipt(receipt_info)