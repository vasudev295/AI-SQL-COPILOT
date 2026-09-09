from pathlib import Path
import sqlite3, random
from datetime import date, timedelta

DB = Path(__file__).parent / "business.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE products (
 product_id INTEGER PRIMARY KEY,
 product_name TEXT NOT NULL,
 category TEXT NOT NULL,
 unit_price REAL NOT NULL
);

CREATE TABLE customers (
 customer_id INTEGER PRIMARY KEY,
 customer_name TEXT NOT NULL,
 region TEXT NOT NULL
);

CREATE TABLE sales (
 sale_id INTEGER PRIMARY KEY,
 sale_date TEXT NOT NULL,
 product_id INTEGER NOT NULL,
 customer_id INTEGER NOT NULL,
 quantity INTEGER NOT NULL,
 revenue REAL NOT NULL,
 FOREIGN KEY(product_id) REFERENCES products(product_id),
 FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
''')

products = [
(1,"Laptop Pro","Electronics",95000),
(2,"Wireless Mouse","Accessories",1800),
(3,"Mechanical Keyboard","Accessories",6500),
(4,"4K Monitor","Electronics",32000),
(5,"USB-C Hub","Accessories",4200),
(6,"Noise Cancelling Headphones","Audio",14500),
(7,"Webcam HD","Accessories",5200),
(8,"Tablet Air","Electronics",48000)
]
cur.executemany("INSERT INTO products VALUES (?,?,?,?)", products)

regions = ["North","South","East","West"]
customers = [(i, f"Customer {i}", regions[(i-1)%4]) for i in range(1,21)]
cur.executemany("INSERT INTO customers VALUES (?,?,?)", customers)

random.seed(42)
rows=[]; sid=1
for day in range(365):
    d=date(2025,1,1)+timedelta(days=day)
    for _ in range(random.randint(3,8)):
        pid=random.randint(1,8)
        cid=random.randint(1,20)
        qty=random.randint(1,8)
        revenue=round(products[pid-1][3]*qty*random.uniform(.90,1.0),2)
        rows.append((sid,d.isoformat(),pid,cid,qty,revenue))
        sid += 1

cur.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?)", rows)
conn.commit()
conn.close()
print(f"Created {DB} with {len(rows)} sales rows.")
