from app.database.schema import get_schema_text
from app.database.executor import execute_select
from app.security.sql_guard import validate_sql
from app.agents.sql_generator import GeminiSQLGenerator

class QueryOrchestrator:
    def __init__(self):
        self.generator=GeminiSQLGenerator()

    def run(self,question,history=""):
        schema=get_schema_text()
        current=question
        last_error=None

        for attempt in range(3):
            try:
                sql=self.generator.generate_sql(current,schema,history)
                safe,reason=validate_sql(sql)

                if not safe:
                    last_error=reason
                    current=f"{question}\nPrevious SQL rejected: {reason}. Generate corrected read-only SQL."
                    continue

                rows=execute_select(sql)
                explanation=self.generator.explain_result(question,sql,rows)

                return {
                    "sql":sql,"rows":rows,"explanation":explanation,
                    "attempts":attempt+1,"error":None
                }

            except Exception as e:
                last_error=str(e)
                current=f"{question}\nPrevious SQL failed: {e}. Correct and retry."

        return {
            "sql":None,"rows":[],"explanation":None,
            "attempts":3,"error":last_error
        }
