📌 NexusAI Intern Challenge
🚀 Overview

This project simulates an AI-powered telecom customer support backend system.
It demonstrates how modern systems handle customer queries using AI, async processing, parallel data fetching, and intelligent escalation logic.

The implementation focuses on clean architecture, error handling, and scalability, similar to real-world backend systems.

📂 Project Structure
task1/  → AI Message Handler  
task2/  → Database Schema  
task3/  → Async Data Fetcher  
task4/  → Escalation Engine  
🤖 Task 1 – AI Message Handler

An asynchronous system that processes customer messages and returns structured AI responses.

✨ Features

Built using async/await

Returns structured output via MessageResponse dataclass

Handles empty input validation

Integrates AI API (OpenAI)

Includes mock fallback response when API quota is exceeded

Parses structured JSON responses

Supports multi-channel responses:

🎙 Voice → max 2 sentences

💬 Chat / WhatsApp → detailed responses

Implements:

⏱ Timeout handling (10 seconds)

🔁 Retry logic for API failures

⚠️ Note on API Usage

OpenAI API requires billing credits

If quota is exceeded, the system automatically falls back to a mock response

This ensures the system remains fully testable without API credits

🗄 Task 2 – Database Schema

Designed a relational database for a telecom support system.

🧩 Tables

customers → user details

agents → support staff

tickets → issue tracking

messages → conversation logs

⚙️ Highlights

Foreign key relationships

Indexed fields for performance

Supports multiple channels (chat, voice, WhatsApp)

Includes sample data for demonstration

⚡ Task 3 – Async Data Fetcher

Fetches customer-related data from multiple systems in parallel.

🔗 Data Sources

CRM system

Billing system

Network system

✨ Features

Uses asyncio.gather() for concurrency

Simulates real-world API delays

Handles failures using return_exceptions=True

Combines all results into a single structured response

🚀 Benefit

Parallel execution significantly reduces response time compared to sequential calls.

🧠 Task 4 – Escalation Engine

Determines whether a customer issue should be escalated to a human agent.

📌 Rules Implemented

Escalate if AI confidence < 0.5

Escalate if network status is down

Escalate if repeated complaints (≥ 3)

📤 Output

Returns an EscalationResult containing:

escalation decision

reason

priority level

▶️ How to Run
Task 1 – AI Handler
python task1/test_handler.py
Task 3 – Async Fetcher
python task3/data_fetcher.py
Task 4 – Escalation Engine
python task4/escalation.py

🧠 Task 5 – Design Considerations

This project also includes written design responses (ANSWERS.md) addressing real-world system challenges.

Key Highlights:

Handling Partial Transcripts (STT):
A hybrid approach is used where early intent detection runs on partial input, while critical database queries are delayed until sufficient context is available. This balances responsiveness and accuracy.

Knowledge Base Automation Risks:
Automatic addition of high-CSAT resolutions can introduce incorrect or outdated knowledge. To mitigate this, validation, clustering, and periodic review mechanisms are recommended.

Customer Escalation Strategy:
In cases of highly negative sentiment or repeated complaints, the system prioritizes empathy and immediate escalation, passing full context to human agents for faster resolution.

System Improvement Focus:
A feedback-driven learning loop is identified as the most impactful improvement, enabling continuous optimization of AI responses based on real interactions.
