# agents/json_agent.py

class JSONAgent:
    def __init__(self, memory_store):
        self.memory_store = memory_store

    def process(self, json_data):
        required_fields = ["sender", "intent", "data"]
        missing = [field for field in required_fields if field not in json_data]
        if missing:
            print(f"JSON Agent: Missing fields: {missing}")
        else:
            print("JSON Agent: Successfully processed structured JSON.")
