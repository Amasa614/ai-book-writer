import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_book_to_pdf(book_content, output_dir="book_output"):
    """Save the generated book content to a PDF file."""
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    pdf_file_path = os.path.join(output_dir, "full_book.pdf")
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2.0, height - 50, "Generated Book")

    c.setFont("Helvetica", 12)
    y_position = height - 80  # Start writing below the title

    for chapter in book_content:
        # Add chapter title
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, y_position, f"Chapter {chapter['chapter_number']}: {chapter['title']}")
        y_position -= 20

        # Add chapter content with line wrapping
        c.setFont("Helvetica", 12)
        chapter_text = chapter['content'].replace("\n", " ")
        words = chapter_text.split(' ')
        current_line = ""

        for word in words:
            if c.stringWidth(current_line + word, "Helvetica", 12) < 450:
                current_line += word + " "
            else:
                c.drawString(72, y_position, current_line)
                y_position -= 15
                current_line = word + " "
            
            if y_position < 50:  # Start a new page if needed
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 80

        if current_line:
            c.drawString(72, y_position, current_line)
            y_position -= 30

    c.save()
    print(f"Full book saved to {pdf_file_path}")
