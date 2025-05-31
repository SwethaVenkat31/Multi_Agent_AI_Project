# main.py
from memory.shared_memory import SharedMemory
from agents.classifier_agent import ClassifierAgent

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

if __name__ == "__main__":
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)

    print("=== Processing JSON ===")
    json_input = read_file("input_files/sample_json.json")
    classifier.classify_and_route(json_input, source="sample_json.json")

    print("\n=== Processing Email ===")
    email_input = read_file("input_files/sample_email.txt")
    classifier.classify_and_route(email_input, source="sample_email.txt")

    print("\n=== Memory Log ===")
    for entry in memory.fetch_all():
        print(entry)
