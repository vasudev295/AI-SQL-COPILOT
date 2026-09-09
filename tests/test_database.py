from pathlib import Path
import sqlite3

def test_database_exists():
    assert Path("data/business.db").exists()

def test_sales_has_rows():
    conn=sqlite3.connect("data/business.db")
    n=conn.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
    conn.close()
    assert n>0
