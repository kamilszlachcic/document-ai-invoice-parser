# document-ai-invoice-parser

🚀 **FastAPI-powered OCR & document extraction API for invoices**

## ✅ Features
- Upload PDF or image invoice
- Extract fields: `invoice_number`, `date`, `due_date`, `total`, `vendor`
- Return results as JSON

---

## 📦 Installation

### Local (requires Tesseract installed)
```bash
git clone https://github.com/yourname/document-ai-invoice-parser.git
cd document-ai-invoice-parser
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker build -t invoice-parser .
docker run -p 8000:8000 invoice-parser
```

---

## 📤 Usage (with curl or Postman)
```bash
curl -X POST "http://localhost:8000/predict_invoice/" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample_invoices/invoice1.pdf"
```

## 📥 Response example
```json
{
  "invoice_number": "FV/2025/04/0012",
  "date": "2025-04-16",
  "due_date": "2025-05-16",
  "total": "1400.00",
  "vendor": "ABC Tech Ltd",
  "document_type": "invoice"
}
```

---

## 🔍 To do next
- Add Hugging Face LayoutLMv3-based parser
- Add document classification (invoice, receipt, form)
- Add Azure Blob integration
