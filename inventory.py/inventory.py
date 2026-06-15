# smart inventory management system
import sqlite3

def setup_database():
    conn = sqlite3.connect('viva_store.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, stock INTEGER)''')
    conn.commit()
    conn.close()

def add_product(name, price, stock):
    conn = sqlite3.connect('viva_store.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
    conn.commit()
    conn.close()
    print("\nSuccess: Product added!")

def view_stock():
    conn = sqlite3.connect('viva_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    print("\nID | Name | Price | Stock")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    conn.close()

def main():
    setup_database()
    while True:
        print("\n--- VIVEKANANDA INVENTORY ---")
        print("1. Add | 2. View | 3. Update | 4. Exit")
        choice = input("Select: ")
        
        if choice == '1':
            n = input("Name: ")
            p = float(input("Price: "))
            s = int(input("Stock: "))
            add_product(n, p, s)
        elif choice == '2':
            view_stock()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()