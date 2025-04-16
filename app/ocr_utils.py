import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import io
from app.file_utils import convert_pdf_to_images

async def extract_text_from_file(file):
    content = await file.read()

    if file.filename.endswith(".pdf"):
        images = convert_pdf_to_images(content)
        text = "\n".join([pytesseract.image_to_string(img) for img in images])
    else:
        image = Image.open(io.BytesIO(content)).convert("RGB")
        text = pytesseract.image_to_string(image)

    return text
