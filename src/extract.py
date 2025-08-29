import csv
import os
import sys
from pathlib import Path
from pdfminer.high_level import extract_text


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from utils.logger import get_logger

logger = get_logger()


pdfs = os.listdir("output")
logger.info(f"Extracting text from {len(pdfs)} PDFs...")
if os.path.exists("extracted"):
    pass
else:
    os.mkdir("extracted")

csv_file = os.path.join("extracted", "extracted.csv")

with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["url", "text"])

    for pdf in pdfs:
        if pdf.endswith(".pdf"):
            try:
                text = extract_text(os.path.join("output", pdf))
                writer.writerow([pdf, text])
                logger.info(f"Extracted text from {pdf} successfully.")
            except Exception as e:
                logger.error(f"Failed to extract text from {pdf}: {e}")
