import json

class QueryEngine:
    def __init__(self, schema_file="schema.json"):
        with open(schema_file, "r") as f:
            self.schema = json.load(f)

    def parse_intent(self, user_input: str):
        user_input = user_input.lower()

        # Generic column lookup
        if "make the query for" in user_input or "show" in user_input:
            words = user_input.split()
            for table, info in self.schema.items():
                for col in info["columns"]:
                    if col.lower() in user_input:
                        return {"schema_lookup": table, "column": col}
            return {"schema_lookup": None, "column": None}

        # Example SQL generation
        if "top" in user_input and "customers" in user_input:
            return {"table": "customers", "order_by": "revenue", "limit": 5}

        return None

    def generate_sql(self, intent):
        if intent and "schema_lookup" in intent:
            if intent["schema_lookup"]:
                return f"SELECT {intent['column']} FROM {intent['schema_lookup']};"
            else:
                return "No table contains the requested column."

        if intent and "table" in intent:
            return f"SELECT * FROM {intent['table']} ORDER BY {intent['order_by']} DESC LIMIT {intent['limit']};"

        return "Unable to generate SQL. Please clarify."
