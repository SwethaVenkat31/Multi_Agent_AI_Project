# Multi-Agent AI System

This is a multi-agent system that:
- Classifies files (email, JSON)
- Uses specialized agents to extract structured data
- Logs everything into a shared memory system

## Folder Structure

- `agents/`: Classifier, Email, and JSON agents
- `memory/`: Shared memory log
- `input_files/`: Sample input files
- `main.py`: Runner script

## How to Run

```bash
python main.py

---
multi_agent_ai_project/
├── agents/
├── memory/
├── input_files/
├── main.py
├── README.md
└── requirements.txt

## 🚀 Final Step: Test It!

Run this in your terminal:

```bash
python main.py


## Agents
- **Classifier Agent:** Detects format & intent, routes to correct agent.
- **Email Agent:** Extracts subject, sender, urgency.
- **JSON Agent:** Validates and processes structured JSON.

## How to Run
```bash
cd multi_agent_ai_project
python main.py
