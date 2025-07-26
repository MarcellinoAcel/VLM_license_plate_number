# 🚘 VLM License Plate Recognition with LMStudio

A simple yet powerful implementation of license plate recognition using a Visual Language Model (VLM) via [LMStudio](https://lmstudio.ai). This project uses the `qwen2-vl-2b-instruct` model to extract license plate numbers from images.

---

## 📦 Features

- 🧠 Multimodal Inference with Qwen2-VL via LMStudio
- 📸 OCR on Indonesian License Plates
- 📊 Evaluation with Ground Truth & Character Error Rate (CER)
- ✅ Compatible with JSON-based configuration

---

## ⚙️ Requirements

- [Python 3.10+](https://www.python.org/downloads/)
- [LMStudio](https://lmstudio.ai)
- A downloaded and running model (e.g., `qwen2-vl-2b-instruct`)

---

## 🧠 Model Setup (LMStudio)

1. **Install LMStudio**  
   Download from [https://lmstudio.ai](https://lmstudio.ai) and install it.

2. **Load the Model**  
   Search and load `qwen2-vl-2b-instruct` in LMStudio.

3. **Run LMStudio API Server**  
   Make sure LMStudio is running and the API is available at:
