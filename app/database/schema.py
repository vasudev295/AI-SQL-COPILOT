from sqlalchemy import inspect
from app.database.connection import engine

def get_schema_text():
    inspector = inspect(engine)
    lines=[]
    for table in inspector.get_table_names():
        lines.append(f"TABLE {table}")
        for col in inspector.get_columns(table):
            lines.append(f"  - {col['name']} ({col['type']})")
    return "\n".join(lines)
