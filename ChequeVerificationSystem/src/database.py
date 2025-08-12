import sqlite3
import os
from src.verify import compare_signatures
from src.preprocess import extract_signature

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "cheque_verification.db")
SIGNATURE_DIR = os.path.join(BASE_DIR, "..", "signatures")
IMAGE_PATH = os.path.join(BASE_DIR, "..", "images", "original.jpg")

if not os.path.exists(SIGNATURE_DIR):
    os.makedirs(SIGNATURE_DIR)

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cheques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        micr_code TEXT UNIQUE,
        signature_path TEXT
    )''')
    conn.commit()
    conn.close()

def store_or_verify_cheque(micr_code):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT signature_path FROM cheques WHERE micr_code=?", (micr_code,))
    result = cursor.fetchone()

    # Prepare new signature path 
    signature_filename = f"{micr_code}_sign.png"
    signature_path = os.path.join(SIGNATURE_DIR, signature_filename)
    
    # Extract the signature
    print("🖼️ Extracting signature from cheque...")
    extracted_path = extract_signature(image_path=IMAGE_PATH, output_path=signature_path)
    
    if not extracted_path:
        print("❌ Signature extraction failed.")
        conn.close()
        return

    if result:
        existing_path = result[0]
        print("🔍 MICR exists. Comparing signatures...")
        is_match, score = compare_signatures(existing_path, signature_path)

        if is_match:
            print(f"✅ Signatures match. Score: {score:.2f}")
        else:
            print(f"❌ Signatures do NOT match. Score: {score:.2f}")
            print(" Removing new unmatched signature.")
            os.remove(signature_path)
    else:
        cursor.execute("INSERT INTO cheques (micr_code, signature_path) VALUES (?, ?)", (micr_code, signature_path))
        conn.commit()
        print("✅ New cheque data saved.")

    conn.close()

def get_signature_path(micr_code):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT signature_path FROM cheques WHERE micr_code=?", (micr_code,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
