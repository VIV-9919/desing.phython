import sqlite3
import pandas as pd # Excel के लिए

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
    print("\n✅ Success: Product added!")

def view_stock():
    conn = sqlite3.connect('viva_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    print("\nID | Name | Price | Stock")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    conn.close()

def update_stock(p_id, new_quantity):
    conn = sqlite3.connect('viva_store.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_quantity, p_id))
    conn.commit()
    conn.close()
    print("\n🔄 Success: Stock updated!")

# --- ADVANCED FEATURE: EXCEL EXPORT ---
def export_to_excel():
    conn = sqlite3.connect('viva_store.db')
    df = pd.read_sql_query("SELECT * FROM products", conn)
    df.to_csv('inventory_report.csv', index=False)
    conn.close()
    print("\n📂 Success: 'inventory_report.csv' created! Check your folder.")

def main():
    setup_database()
    while True:
        print("\n--- VIVEKANANDA SMART INVENTORY ---")
        print("1. Add Product")
        print("2. View Stock")
        print("3. Update Stock (by ID)")
        print("4. Export to Excel (CSV)")
        print("5. Exit")
        
        choice = input("Select: ")
        
        if choice == '1':
            n = input("Name: ")
            p = float(input("Price: "))
            s = int(input("Stock: "))
            add_product(n, p, s)
        elif choice == '2':
            view_stock()
        elif choice == '3':
            i = int(input("Enter Product ID to update: "))
            q = int(input("Enter New Quantity: "))
            update_stock(i, q)
        elif choice == '4':
            export_to_excel()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()