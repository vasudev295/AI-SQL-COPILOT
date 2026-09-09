import re
import sqlglot
from sqlglot import exp

BLOCKED=re.compile(
 r"\b(DROP|DELETE|UPDATE|INSERT|ALTER|TRUNCATE|CREATE|ATTACH|DETACH|REPLACE|GRANT|REVOKE)\b",
 re.I
)

def validate_sql(sql):
    sql=sql.strip().rstrip(";")
    if not sql: return False,"Empty SQL query."
    if BLOCKED.search(sql): return False,"Only read-only SQL is allowed."
    if not re.match(r"^(SELECT|WITH)\b",sql,re.I):
        return False,"Only SELECT/WITH queries are allowed."
    try:
        statements=sqlglot.parse(sql,read="sqlite")
        if len(statements)!=1: return False,"Only one SQL statement is allowed."
        for node in statements[0].walk():
            if isinstance(node,(exp.Insert,exp.Update,exp.Delete,exp.Drop,exp.Create,exp.Alter)):
                return False,"Write/DDL operation detected."
    except Exception as e:
        return False,f"SQL parsing failed: {e}"
    return True,"SQL is safe."
