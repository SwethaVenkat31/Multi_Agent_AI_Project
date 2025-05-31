# agents/classifier_agent.py
import json
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent

class ClassifierAgent:
    def __init__(self, memory_store):
        self.json_agent = JSONAgent(memory_store)
        self.email_agent = EmailAgent(memory_store)
        self.memory_store = memory_store

    def classify_and_route(self, raw_input, source="input"):
        try:
            data = json.loads(raw_input)
            input_type = "JSON"
            intent = data.get("intent", "Unknown")
            self.memory_store.log(source, input_type, data)
            self.json_agent.process(data)
        except json.JSONDecodeError:
            if "Subject:" in raw_input:
                input_type = "Email"
                intent = "RFQ" if "RFQ" in raw_input else "Unknown"
                self.memory_store.log(source, input_type, {"intent": intent})
                self.email_agent.process(raw_input)
            else:
                print("Classifier: Unsupported input type.")
