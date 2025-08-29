import csv
import os
import sys
import PyPDF2

# Increase field size limit safely - MOVED AFTER IMPORTS
csv.field_size_limit(2**31 - 1)

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + ' '
            return text.strip()
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return ""

def extract_texts_from_folder(folder_path):
    """Extract text from all PDFs in a folder.
    Returns a list of texts."""
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    pdf_files.sort()
    texts = []
    
    if not pdf_files:
        print("⚠️ No PDF files found in the folder.")
        return texts
    
    for i, pdf_file in enumerate(pdf_files):
        pdf_path = os.path.join(folder_path, pdf_file)
        print(f"Processing {pdf_file} ({i+1}/{len(pdf_files)})...")
        text = extract_text_from_pdf(pdf_path)
        texts.append(text if text else "")
    
    return texts

def merge_urls_and_texts(input_csv, output_csv, folder_path):
    """Read URLs from CSV and add PDF texts in a new column, write to output CSV."""
    # First extract all PDF texts
    pdf_texts = extract_texts_from_folder(folder_path)
    
    # Now process the CSV files
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, \
         open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ["urls", "text"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        row_count = 0
        for i, row in enumerate(reader):
            url = row.get("urls", "")
            # Get the corresponding text (use empty string if index out of range)
            text = pdf_texts[i] if i < len(pdf_texts) else ""
            writer.writerow({"urls": url, "text": text})
            row_count += 1
    
    print(f"\n✅ Finished! Created {output_csv} with {row_count} rows.")
    
    # Print final results (first few rows)
    print("\nFirst few rows of the output:")
    with open(output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i < 5:  # Show first 5 rows
                print(f"Row {i}: {row}")
            else:
                break

if __name__ == "__main__":
    input_csv = r"C:\\Personal\\Adam Van Blerk\\University\\3rd Year\\CS312\\SE\\Project\\Code\\Extract folders\\pdf-extraction\\data\\pdfs.csv"
    output_csv = r"C:\\Personal\\Adam Van Blerk\\University\\3rd Year\\CS312\\SE\\Project\\Code\\Extract folders\\pdf-extraction\\output\\extractedU&T\\output.csv"
    folder_path = r"C:\\Personal\\Adam Van Blerk\\University\\3rd Year\\CS312\\SE\\Project\\Code\\Extract folders\\pdf-extraction\\output\\pdfextract"
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    
    merge_urls_and_texts(input_csv, output_csv, folder_path)