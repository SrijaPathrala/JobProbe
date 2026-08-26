import re

# Each rule checks the text and, if triggered, returns a flag dict.
# Severity points: high=30, medium=15, low=5


def check_payment_request(text: str):
    keywords = [
        "registration fee", "security deposit", "processing fee",
        "training fee", "pay to join", "refundable deposit",
        "pay a fee", "advance payment", "deposit amount"
    ]
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            return {
                "flag": "payment_request",
                "severity": "high",
                "points": 30,
                "explanation": "The message asks for money upfront. Legitimate employers never ask candidates to pay to get a job."
            }
    return None


def check_unrealistic_salary(text: str):
    text_lower = text.lower()
    has_no_experience = "no experience" in text_lower or "fresher" in text_lower
    salary_match = re.search(r"(₹|Rs\.?|INR)\s?([\d,]+)", text)

    if salary_match and has_no_experience:
        amount_str = salary_match.group(2).replace(",", "")
        try:
            amount = int(amount_str)
            if amount >= 50000:  # threshold: 50k+ with "no experience" is suspicious
                return {
                    "flag": "unrealistic_salary",
                    "severity": "high",
                    "points": 30,
                    "explanation": "A very high salary combined with 'no experience needed' is a common scam pattern."
                }
        except ValueError:
            pass
    return None


def check_urgency_pressure(text: str):
    keywords = [
        "immediate joining", "limited seats", "limited slots", "act now", "hurry",
        "urgent requirement", "apply within", "only today", "last chance",
        "few slots left", "hurry up", "don't miss", "expires soon", "join immediately"
    ]
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            return {
                "flag": "urgency_pressure",
                "severity": "medium",
                "points": 15,
                "explanation": "The message uses urgency or pressure tactics to rush your decision, a common scam technique."
            }
    return None


def check_suspicious_email(text: str, email: str):
    if not email:
        return None
    free_providers = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
    domain = email.split("@")[-1].lower()
    if domain in free_providers:
        return {
            "flag": "suspicious_email",
            "severity": "medium",
            "points": 15,
            "explanation": f"The recruiter uses a free email provider ({domain}) instead of an official company domain."
        }
    return None


def check_suspicious_urls(urls: list):
    shorteners = ["bit.ly", "tinyurl.com", "t.co", "is.gd", "cutt.ly"]
    for url in urls:
        for s in shorteners:
            if s in url:
                return {
                    "flag": "suspicious_url",
                    "severity": "medium",
                    "points": 15,
                    "explanation": "The message contains a shortened URL, often used to hide the real destination."
                }
    return None


def check_sensitive_info_request(text: str):
    keywords = [
        "aadhar", "aadhaar", "bank account number", "otp", "cvv",
        "debit card", "credit card number", "pan card number"
    ]
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            return {
                "flag": "sensitive_info_request",
                "severity": "high",
                "points": 30,
                "explanation": "The message asks for sensitive personal/financial information, which legitimate employers don't need before hiring."
            }
    return None


def run_all_rules(text: str, extracted_info: dict) -> list:
    """
    Runs every rule and returns a list of triggered flags (skips None results).
    """
    checks = [
        check_payment_request(text),
        check_unrealistic_salary(text),
        check_urgency_pressure(text),
        check_suspicious_email(text, extracted_info.get("email")),
        check_suspicious_urls(extracted_info.get("urls", [])),
        check_sensitive_info_request(text),
    ]
    return [flag for flag in checks if flag is not None]