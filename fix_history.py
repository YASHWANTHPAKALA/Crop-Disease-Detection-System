import sqlite3

def fix_history():
    # Updated to point to your actual database filename
    conn = sqlite3.connect('crop_app.db')
    cursor = conn.cursor()
    try:
        # Adding the missing timestamp column
        cursor.execute("ALTER TABLE history ADD COLUMN timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
        conn.commit()
        print("Success: timestamp column added to history table.")
    except sqlite3.OperationalError:
        print("Column might already exist or table name is wrong.")
    conn.close()

if __name__ == "__main__":
    fix_history()