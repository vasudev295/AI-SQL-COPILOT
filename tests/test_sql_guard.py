from app.security.sql_guard import validate_sql

def test_select_allowed():
    assert validate_sql("SELECT * FROM sales LIMIT 5")[0]

def test_delete_blocked():
    assert not validate_sql("DELETE FROM sales")[0]

def test_drop_blocked():
    assert not validate_sql("DROP TABLE sales")[0]

def test_multiple_statements_blocked():
    assert not validate_sql("SELECT 1; SELECT 2")[0]
