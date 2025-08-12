import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "cheque_verification.db")

def display_all_cheques():
    if not os.path.exists(DB_PATH):
        print(" Database not found. Please run the main script to create it.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cheques")
    rows = cursor.fetchall()

    if rows:
        print("\n📋 Stored Cheques:\n--------------------------")
        for row in rows:
            print(f"🆔 ID: {row[0]}\n🔢 MICR Code: {row[1]}\n📁 Signature Path: {row[2]}\n")
    else:
        print("📭 No cheque data found in the database.")

    conn.close()


if __name__ == "__main__":
    display_all_cheques()
