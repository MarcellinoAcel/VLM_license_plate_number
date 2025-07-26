import os
import csv
import base64
import requests
from PIL import Image
import lmstudio as lms
import difflib
from tqdm import tqdm

# === Konfigurasi ===
DATASET_DIR = r"C:\Users\user\Documents\coding\python\computer_vision\VLM_license_plate_number\Indonesian License Plate Recognition Dataset\images\test"
GROUND_TRUTH_CSV = r"C:\Users\user\Documents\coding\python\computer_vision\VLM_license_plate_number\Indonesian License Plate Recognition Dataset\ground_truth.csv"
OUTPUT_CSV = "ocr_result.csv"
SERVER_API_HOST = "localhost:1234"
SERVER_URL = "http://localhost:1234/v1/chat/completions"
VLM_MODEL_NAME = "qwen2-vl-2b-instruct"

# # === Inisialisasi LMStudio Client ===
# lms.configure_default_client(SERVER_API_HOST)
# model = lms.llm(VLM_MODEL_NAME)

# === Fungsi untuk menghitung CER ===
def calculate_cer(ground_truth, prediction):
    matcher = difflib.SequenceMatcher(None, ground_truth, prediction)
    opcodes = matcher.get_opcodes
    S = D = I = 0
    for opcode, i1, i2, j1, j2 in matcher.get_opcodes():
        if opcode == 'replace':
            S += max(i2 - i1, j2 - j1)
        elif opcode == 'delete':
            D += i2 - i1
        elif opcode == 'insert':
            I += j2 - j1
    N = len(ground_truth)
    CER = round((S + D + I) / N, 4)
    formula = f"CER = ({S}+{D}+{I}/{N})"
    return CER, formula
 

# === Load Ground Truth ===
def load_ground_truth(csv_path):
    """Load ground truth from CSV into dictionary"""
    gt_dict = {}
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            gt_dict[row["image"]] = row["ground_truth"]
    return gt_dict

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# === Prediksi OCR dengan VLM ===
def ocr_image(image_path):
    """Send image to VLM and extract plate number"""
    try:
        # encode image to base64
        image_base64 = encode_image_to_base64(image_path)

        # prepare payload
        payload = {
            "model":VLM_MODEL_NAME,
            "messages":[
                {
                    "role": "user",
                    "content":[
                        {
                            "type": "image_url",
                            "image_url":{
                                "url":f"data:iamge/jpeg;base64,{image_base64}"
                            }
                        },
                        {
                            "type": "text",
                            "text": "What is the license plate number shown in this image? Respond only with the plate number."
                        }
                    ]
                }
            ],
            "stream": False
        }

        response = requests.post(SERVER_URL,json=payload)
        response.raise_for_status()
        result = response.json()["choices"][0]["message"]["content"]
        return result.strip().replace(" ", "").upper()
    except Exception as e:
        print(f"Error processing {os.path.basename(image_path)}: {str(e)}")
        return "ERROR"


# === Main ===
def main():
    ground_truths = load_ground_truth(GROUND_TRUTH_CSV)
    if not ground_truths:
        print("❌ No ground truth data loaded. Exiting.")
        return
    image_files = list(ground_truths.keys())
    
    with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["image", "ground_truth", "prediction", "CER_score"])

        for image_name in tqdm(image_files, desc="Processing Plates"):
            image_path = os.path.join(DATASET_DIR, image_name)
            gt_text =ground_truths[image_name]

            # Get Prediction
            pred_text = ocr_image(image_path)

            # calculate CER
            cer = calculate_cer(gt_text, pred_text)

            # Write results
            writer.writerow([image_name, gt_text, pred_text, cer])

            # print progress
            print(f"{image_name}=>GT:{gt_text} | pred:{pred_text} | CER{cer}")

    print(f"\n✅ OCR selesai. Hasil disimpan di {OUTPUT_CSV}")

if __name__ == "__main__":
    main()