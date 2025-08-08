import os
import sys
from pathlib import Path
from pdfminer.high_level import extract_text


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


from utils.logger import get_logger

logger = get_logger()


pdf = os.listdir("output/")[4]

logger.info(f"Extracting text from {pdf}")

text = extract_text(f"output/{pdf}")

logger.info(text)
