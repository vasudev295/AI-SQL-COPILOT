from sqlalchemy import text
from app.database.connection import engine

def execute_select(sql):
    with engine.connect() as conn:
        result=conn.execute(text(sql))
        return [dict(row._mapping) for row in result.fetchall()]
