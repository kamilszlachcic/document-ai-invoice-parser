import re
from typing import Dict

DATE_REGEX = r"(\d{4}[-/.]\d{2}[-/.]\d{2}|\d{2}[-/.]\d{2}[-/.]\d{4})"
AMOUNT_REGEX = r"(?:total|amount)\D{0,10}(\d+[\.,]\d{2})"
INVOICE_REGEX = r"(?:invoice\s*(?:no\.|number)?\s*[:#]?\s*)([\w/-]+)"
DUE_DATE_REGEX = r"(?:due date|pay by|payment due|termin płatności|należy zapłacić do)[^\d]{0,10}(%s)" % DATE_REGEX

def extract_invoice_data(text: str) -> Dict[str, str]:
    def find(pattern, text, flags=re.IGNORECASE):
        match = re.search(pattern, text, flags)
        return match.group(1).strip() if match else "Not found"

    invoice_number = find(INVOICE_REGEX, text)
    invoice_date = find(DATE_REGEX, text)
    due_date = find(DUE_DATE_REGEX, text)
    total = find(AMOUNT_REGEX, text)

    # Vendor heurystyka: pierwsza linia zawierająca 'Ltd', 'Sp. z o.o.' itp.
    vendor = "Not found"
    for line in text.splitlines():
        if any(x in line.lower() for x in ["ltd", "gmbh", "inc", "sp. z o.o."]):
            vendor = line.strip()
            break

    return {
        "invoice_number": invoice_number,
        "date": invoice_date,
        "due_date": due_date,
        "total": total,
        "vendor": vendor,
        "document_type": "invoice"
    }
