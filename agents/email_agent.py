# agents/email_agent.py
import re

class EmailAgent:
    def __init__(self, memory_store):
        self.memory_store = memory_store

    def process(self, email_content):
        subject = re.search(r'Subject: (.*)', email_content)
        sender = re.search(r'From: (.*)', email_content)
        urgency = "High" if "urgent" in email_content.lower() else "Normal"

        print(f"Email Agent: Subject='{subject.group(1) if subject else 'Unknown'}'")
        print(f"Email Agent: Sender='{sender.group(1) if sender else 'Unknown'}'")
        print(f"Email Agent: Urgency='{urgency}'")
