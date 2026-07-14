import sqlite3

# Updated to point to your actual database filename
db_path = 'crop_app.db' 

def upgrade_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Adding new columns...")
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN username TEXT")
        cursor.execute("ALTER TABLE users ADD COLUMN age INTEGER")
        cursor.execute("ALTER TABLE users ADD COLUMN location TEXT")
        conn.commit()
        print("Success! Columns added.")
    except sqlite3.OperationalError as e:
        print(f"Note: {e} (This usually means the columns already exist)")
    
    conn.close()

if __name__ == "__main__":
    upgrade_db()