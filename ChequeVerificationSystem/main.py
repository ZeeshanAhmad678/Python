import sys
import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from src.database import create_database, store_or_verify_cheque

# Unicode output in terminal
sys.stdout.reconfigure(encoding='utf-8')

def ask_micr_popup(prompt="Enter MICR code:"):
    root = tk.Tk()
    root.withdraw()
    micr_code = simpledialog.askstring("MICR Code Input", prompt)
    if not micr_code:
        messagebox.showerror("Error", "MICR code cannot be empty.")
        sys.exit(0)
    return micr_code.strip()

# Step 1: Create database if it doesn't exist
print("📦 Creating the database...")
create_database()

# Step 2: Ask MICR code first
micr_code = ask_micr_popup("⌨️ Enter MICR code for the cheque:")

# Step 3: Process cheque (compare or store depending on MICR)
print("🔍 Processing cheque for MICR code:", micr_code)
store_or_verify_cheque(micr_code)
