# 🧪 Lab Report Extractor - FastAPI 🚀

A powerful and lightweight FastAPI service to **extract lab test names, values, and reference ranges** from medical report images using OCR, image preprocessing, and regex-based parsing — **without using any LLMs**.

<p align="center">
  <img width="1440" alt="Screenshot 2025-04-29 at 1 19 38 PM" src="https://github.com/user-attachments/assets/c46e3986-7d09-4e89-87da-986f86ad0172" />
  <img width="1438" alt="Screenshot 2025-04-29 at 1 20 28 PM" src="https://github.com/user-attachments/assets/8ac0433b-d86c-45b8-ab64-f635879c3038" />
  <img width="1440" alt="Screenshot 2025-04-29 at 1 20 06 PM" src="https://github.com/user-attachments/assets/d3140f56-ae09-430c-8495-446f7a2e2cc6" />
  <img width="1410" alt="Screenshot 2025-04-29 at 1 21 26 PM" src="https://github.com/user-attachments/assets/e6c46d37-009e-4912-89f8-4fb2ec321852" />
</p>

---

## 📌 Project Overview

This project solves the challenge of reading **lab report images** (PNG/JPG) and extracting:
- Test Name (e.g., Hemoglobin)
- Test Value (e.g., 13.2)
- Bio Reference Range (e.g., 12.0 - 15.5)
- Flag for Out-of-Range values

It exposes a **REST API** with a `/get-lab-tests` POST endpoint and a custom web UI for uploading images.

---

## 🌟 Features

- 🧠 Accurate OCR extraction using Tesseract
- 🧹 Image preprocessing for noise reduction
- 🧬 Regex-based smart parsing of test data
- 📊 Auto flag for values out of reference range
- 🖼️ Beautiful custom upload UI
- ⚡ FastAPI-powered backend with OpenAPI docs
- ☁️ Deployed & hosted via Render

---

## 🚀 Live Demo
- 🔗 **Swagger Docs:** [https://lab-report-extractor-fastapi.onrender.com/docs](https://lab-report-extractor-fastapi-production.up.railway.app/docs#/default/get_lab_tests_get_lab_tests_post)

---

## 🔧 Tech Stack

| Technology     | Purpose                            |
|----------------|------------------------------------|
| Python         | Core programming language          |
| FastAPI        | Web framework for building the API |
| Uvicorn        | ASGI server to serve FastAPI       |
| OpenCV         | Image preprocessing                |
| Tesseract OCR  | Extracting text from image         |
| Regex          | Parsing extracted text             |
| Tailwind CSS   | Styling the custom frontend UI     |
| Render         | Cloud deployment platform          |

---

## 🛠️ Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/ps0821/lab-report-extractor-fastapi.git
cd lab-report-extractor-fastapi

# 2. Create virtual environment
python3 -m venv bfhl_env
source bfhl_env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the API
uvicorn app.main:app --reload
