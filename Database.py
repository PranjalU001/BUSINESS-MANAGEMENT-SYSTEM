# create_db.py
import sqlite3 as sq

def create_database():
    con = sq.connect('bms_app.db')
    cur = con.cursor()

    # Create Employee Table
    cur.execute('''CREATE TABLE IF NOT EXISTS employee (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Email TEXT,
                Address TEXT,
                Gender TEXT,
                Password TEXT,
                Contact TEXT,
                JoinDate TEXT,
                UserType TEXT)''')

# Commit the changes and close the connection
    con.commit()
    con.close()
    # Create Supplier Table
    cur.execute('''CREATE TABLE IF NOT EXISTS supplier (
                    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Address TEXT,
                    Contact TEXT,
                    Email TEXT)''')

    con.commit()
    con.close()
# Create inventory table
    con = sq.connect('bms.db')
    cur = con.cursor()

        # Create table for products
    cur.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Brand TEXT NOT NULL,
                        Type TEXT NOT NULL,
                        Price REAL NOT NULL,
                        Batch_Code TEXT NOT NULL,
                        Quantity INTEGER NOT NULL
                    )''')

    con.commit()
            # Create table for sale
    conn = sq.connect('bms_app.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sale (
                            rowid INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT NOT NULL,
                            revenue REAL NOT NULL
                          )''')
    con.commit()
    con.close()

        # Commit changes
    
    def __del__(self):
        self.conn.close()
if __name__ == "__main__":
    create_database()

