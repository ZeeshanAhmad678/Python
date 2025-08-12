#Cheque Verification System
## Semester Project
## 📜 Purpose of Each File and When to Use Them

### **`main.py`**
- **Purpose**:  
  Main program that ties all components together.  
  Handles MICR code input, signature extraction, and verification.
- **When to Use**:  
  Run this file to perform cheque verification or store a new signature.

---

### **`src/database.py`**
- **Purpose**:  
  - Creates and manages the SQLite database (`cheque_verification.db`).
  - Checks if MICR already exists in the database.
  - Saves new signature if MICR is new.
  - Compares signatures if MICR exists.
- **When to Use**:  
  This file is **imported** by `main.py` — you don’t run it directly.

---

### **`src/preprocess.py`**
- **Purpose**:  
  Extracts the cheque’s signature from a predefined ROI using:
  - Grayscale conversion
  - Contrast adjustment
  - Canny edge detection
- **When to Use**:  
  Called by `database.py` automatically during verification or storage.

---

### **`src/verify.py`**
- **Purpose**:  
  - Loads two signature images.
  - Uses **SIFT feature extraction**.
  - Performs keypoint matching to determine similarity.
- **When to Use**:  
  Automatically called when verifying an existing MICR in the database.

---

### **`src/display_cheques.py`**
- **Purpose**:  
  Lists all stored cheques (MICR codes + file paths) from the database.
- **When to Use**:  
  Run manually to inspect all stored data:
  ```bash
  python src/display_cheques.py

```
git clone https://github.com/yourusername/cheque-verification-system.git
cd ChequeVerificationSystem
pip install opencv-python numpy pillow
python main.py
```
