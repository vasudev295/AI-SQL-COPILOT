import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiSQLGenerator:
    def __init__(self):
        key=os.getenv("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("GEMINI_API_KEY missing. Add it to .env")
        self.client=genai.Client(api_key=key)
        self.model=os.getenv("GEMINI_MODEL","gemini-2.5-flash")

    def generate_sql(self,question,schema,history=""):
        prompt=f'''
You are an expert SQLite data analyst.

SCHEMA:
{schema}

CONVERSATION:
{history or "None"}

QUESTION:
{question}

Rules:
- Return ONLY one SQL query.
- Use only schema tables and columns.
- Only SELECT or WITH.
- Never modify data.
- revenue means sales.revenue.
- sale_date is YYYY-MM-DD.
- Use clear aliases.
'''
        response=self.client.models.generate_content(model=self.model,contents=prompt)
        sql=response.text.strip()
        if sql.startswith("```"):
            sql=sql.replace("```sql","").replace("```","").strip()
        return sql

    def explain_result(self,question,sql,rows):
        prompt=f'''
Act as a business analyst.
Question: {question}
SQL: {sql}
Rows: {rows[:30]}
Give a concise business-friendly answer. Use only values in the result.
'''
        return self.client.models.generate_content(
            model=self.model,contents=prompt
        ).text.strip()
