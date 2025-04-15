import logging
import re
import argparse
import pdfplumber

# Suppress warnings 
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# Mapping for scale keywords (used in contextual text like "in millions")
SCALE_KEYWORDS = {
    "million": 1_000_000,
    "millions": 1_000_000,
    "billion": 1_000_000_000,
    "billions": 1_000_000_000,
    "thousand": 1_000,
    "thousands": 1_000
}

def parse_number_with_suffix(text: str) -> list:
    """
    Extract numbers that use scale suffixes (e.g., 134.0M, 5.2B).
    Returns a list of tuples: (original_number, scaled_number, multiplier).
    """
    # Match patterns like "56.7M", "1.2B", etc.
    pattern = re.compile(r'\b(\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+\.\d+|\d+)([KkMmBbTt])\b')

    # Define the meaning of each suffix
    suffix_multipliers = {
        'k': 1_000, 'K': 1_000,
        'm': 1_000_000, 'M': 1_000_000,
        'b': 1_000_000_000, 'B': 1_000_000_000,
        't': 1_000_000_000_000, 'T': 1_000_000_000_000
    }

    results = []
    for match in pattern.finditer(text):
        raw_num = float(match.group(1).replace(',', ''))  # remove commas for clean float conversion
        suffix = match.group(2)
        multiplier = suffix_multipliers.get(suffix, 1)
        scaled_value = raw_num * multiplier
        results.append((raw_num, scaled_value, multiplier))
    
    return results


def find_scale_factor(text: str) -> int:
    """
    Finds the scale keyword that appears last in the page.
    Returns its corresponding multiplier.
    NOTE - this only works if there's one scaling keyword in the page. For ex.  
    <
    Section 1: (in billions)
    ... data ...
    Section 2: (in thousands)
    ... data ...>

    The chosen factor would be thousands. Would have to handle it line by line to fix to have data in section 1 be billions. 
    """
    text_lower = text.lower()
    last_pos = -1
    chosen_factor = 1

    for word, factor in SCALE_KEYWORDS.items():
        for pattern in [f"in {word}", f"({word})"]:
            index = text_lower.rfind(pattern)
            if index > last_pos:
                last_pos = index
                chosen_factor = factor

    return chosen_factor


def extract_numbers(text: str) -> list:
    """
    Extract plain numbers from the text.
    Returns a list of floats.
    """
    pattern = re.compile(r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?|\b\d+\.\d+|\b\d+")
    return [float(num.replace(",", "")) for num in pattern.findall(text)]


def find_largest_number_in_pdf(pdf_path: str, top_n: int = 1) -> list:
    """
    Finds top N scaled numbers in the PDF.
    Applies suffix scale if present (e.g., 56.7M),
    otherwise applies context page scale (e.g., 'in millions' on page).
    Reason for doing both is if there's only suffix scale, then we'd miss 134.0 on a page that says "in millions"
    and if only context page scale, then it'll incorrectly scale 134.0M using page context scale factor. 
    Parameters:
        pdf_path (str): Path to the PDF file.
        top_n (int): Number of top results to return.
    
    Returns:
        List of top N scaled values with page num.
    """
    top_values = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue

            # 1. Get all numbers with suffixes like 56.7M
            suffix_numbers = parse_number_with_suffix(text)
            suffix_values = set()
            for raw_num, scaled_value, multiplier in suffix_numbers:
                # add scaled value, page number, raw number, the scale factor/multiplier
                top_values.append((scaled_value, i + 1, raw_num, multiplier))
                suffix_values.add(raw_num)

            # 2. Handle numbers with contextual page scale ("in millions")
            numbers = extract_numbers(text)
            scale_factor = find_scale_factor(text)
            for num in numbers:
                if num in suffix_values: # already handled with suffix like M/B/K
                    #print("Already handled")
                    continue
                scaled = num * scale_factor
                top_values.append((scaled, i + 1, num, scale_factor))

    top_values.sort(reverse=True, key=lambda x: x[0])
    return top_values[:top_n]




def find_largest_raw_numbers(pdf_path: str, top_n=1) -> list:
    """
    Finds the top N largest raw numbers in the PDF.
    Returns a list of tuples: (raw_number, page_number)
    """
    raw_values = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue

            numbers = extract_numbers(text)
            for num in numbers:
                raw_values.append((num, i + 1))

    raw_values.sort(reverse=True, key=lambda x: x[0])
    return raw_values[:top_n]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract top N largest scaled and raw numbers from a PDF.")
    parser.add_argument("--top", type=int, default=1, help="Number of top results to display (default: 1)")
    args = parser.parse_args()

    PDF_PATH = "data.pdf"

    print(f"\n Top {args.top} Scaled Numbers:")
    top_scaled = find_largest_number_in_pdf(PDF_PATH, top_n=args.top)
    for rank, (scaled, page, *_rest) in enumerate(top_scaled, 1):
        print(f"{rank}. {scaled:,.2f} (page {page})")

    print(f"\n Top {args.top} Raw Numbers:")
    top_raw = find_largest_raw_numbers(PDF_PATH, top_n=args.top)
    for rank, (num, page) in enumerate(top_raw, 1):
        print(f"{rank}. {num:,.2f} (page {page})")
