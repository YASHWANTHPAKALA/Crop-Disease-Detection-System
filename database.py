import sqlite3

def init_db():
    conn = sqlite3.connect('crop_app.db')
    
    # Enable foreign key support in SQLite
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    
    # User Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       username TEXT,
                       email TEXT UNIQUE NOT NULL, 
                       password TEXT NOT NULL,
                       age INTEGER,
                       location TEXT)''')
                       
    # Migrate existing databases by adding new columns
    for col, col_type in [('username', 'TEXT'), ('age', 'INTEGER'), ('location', 'TEXT')]:
        try:
            cursor.execute(f'ALTER TABLE users ADD COLUMN {col} {col_type}')
        except sqlite3.OperationalError:
            pass # Column already exists
                       
    # History Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS history 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       user_id INTEGER NOT NULL, 
                       crop_type TEXT NOT NULL, 
                       disease TEXT NOT NULL, 
                       confidence REAL NOT NULL, 
                       timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                       FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()