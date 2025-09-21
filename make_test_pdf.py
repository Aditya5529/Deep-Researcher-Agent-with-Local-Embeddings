# scripts/make_test_pdf.py
from reportlab.pdfgen import canvas

def create_pdf(path="data/test.pdf"):
    c = canvas.Canvas(path)
    c.drawString(100, 750, "Deep Researcher Agent Test PDF")
    c.drawString(100, 730, "This document explains how AI can help in research.")
    c.drawString(100, 710, "Artificial intelligence allows automated text analysis, summarization, and retrieval.")
    c.drawString(100, 690, "This PDF is created just for testing your pipeline.")
    c.save()

if __name__ == "__main__":
    create_pdf()
    print("✅ test.pdf created at data/test.pdf")
