import re


def extract_email(text: str):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None


def extract_phone(text: str):
    # Matches common Indian/international phone formats: 10 digits, optional +91, spaces/dashes
    match = re.search(r"(\+?\d{1,3}[-\s]?)?\d{10}", text)
    return match.group(0) if match else None


def extract_urls(text: str):
    urls = re.findall(r"https?://[^\s]+|www\.[^\s]+", text)
    return urls


def extract_salary(text: str):
    # Looks for currency symbols/keywords followed by numbers, e.g. ₹80,000 or $5000 or "50k"
    match = re.search(
        r"(₹|Rs\.?|INR|\$)\s?[\d,]+(\.\d+)?\s?(per\s?(week|month|year|annum))?|"
        r"\d+\s?(k|K)\s?(per\s?(week|month|year|annum))?",
        text
    )
    return match.group(0) if match else None


def extract_all(text: str) -> dict:
    """
    Runs all extractors and returns a single dictionary
    of extracted fields from the job posting text.
    """
    return {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "urls": extract_urls(text),
        "salary": extract_salary(text),
    }