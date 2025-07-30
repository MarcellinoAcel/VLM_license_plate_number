# VLM License Plate Recognition with LMStudio

A simple yet powerful implementation of license plate recognition using a Visual Language Model (VLM) via [LMStudio](https://lmstudio.ai). This project uses the `qwen2-vl-2b-instruct` model to extract license plate numbers from images.

---

## Features

- Multimodal Inference with Qwen2-VL via LMStudio
- OCR on Indonesian License Plates
- Evaluation with Ground Truth & Character Error Rate (CER)
- Compatible with JSON-based configuration

---

## Requirements

- [Python 3.10+](https://www.python.org/downloads/)
- [LMStudio](https://lmstudio.ai)
- A downloaded and running model (e.g., `qwen2-vl-2b-instruct`)

---

## Model Setup (LMStudio)

1. **Install LMStudio**  
   Download from [https://lmstudio.ai](https://lmstudio.ai) and install it.

2. **Load the Model**  
   Search and load `qwen2-vl-2b-instruct` in LMStudio.

3. **Run LMStudio API Server**  
   Run the LMStudio server using command
```bash  
lms server start
```

## Dataset Setup
**Go to this website and download the dataset**
- [kaggle Dataset](https://www.kaggle.com/datasets/juanthomaswijaya/indonesian-license-plate-dataset).

**You can delete the unnecessary folder, cause we only use**
```bash
Indonesian License Plate Recognition Dataset/images/test
```
## Run the code
1. **Run the Groundtruth**
   first thing first you need a ground truth to get the actuall value the.

   example:
<table>
  <tr>
    <th>Image</th>
    <th>Ground Truth</th>
  </tr>
  <tr>
    <td><img src="Indonesian License Plate Recognition Dataset\images\test\test001_1.jpg" width="100"></td>
    <td>B9140BCD</td>
  </tr>
  <tr>
    <td><img src="Indonesian License Plate Recognition Dataset\images\test\test001_2.jpg" width="100"></td>
    <td>B2407UZO</td>
  </tr>
  <tr>
    <td><img src="Indonesian License Plate Recognition Dataset\images\test\test001_3.jpg" width="100"></td>
    <td>B2842PKM</td>
  </tr>
</table>

