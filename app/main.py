from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.ocr_utils import extract_text_from_file
from app.parser import extract_invoice_data
import uvicorn

app = FastAPI()

@app.post("/predict_invoice/")
async def predict_invoice(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    try:
        # OCR
        raw_text = await extract_text_from_file(file)

        # Extract fields
        extracted = extract_invoice_data(raw_text)

        return JSONResponse(content=extracted)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
