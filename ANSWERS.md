---

Q1: Handling Partial Transcripts (STT)

Starting database queries on partial transcripts can improve responsiveness, but it must be done carefully. I would use a hybrid approach where lightweight intent detection runs continuously on partial transcripts, while delaying expensive or critical database queries until the transcript is complete or sufficiently stable.

Partial transcripts are often noisy and incomplete, which can lead to incorrect intent detection and unnecessary database calls. However, they still provide early signals that can be useful for prefetching likely data, such as customer profile or recent tickets.

My approach would include:
- Running fast, low-cost intent estimation on partial inputs  
- Prefetching only high-confidence data in the background  
- Confirming intent before executing final queries  

This balances latency and accuracy. It improves perceived responsiveness while avoiding wasted computation and incorrect results. The key tradeoff is between speed and correctness, and this staged approach optimizes both effectively.

---

Q2: Risks of Auto-Adding to Knowledge Base

Automatically adding resolutions with CSAT ≥ 4 to the knowledge base can improve learning, but it introduces long-term risks.

First, incorrect or context-specific solutions may be added. A resolution that worked in one scenario may not generalize, leading to misleading suggestions. To prevent this, I would implement clustering and validation, ensuring that similar cases exist before promoting a solution.

Second, the system may accumulate outdated or redundant entries over time, reducing the quality of recommendations. To address this, I would introduce periodic review and decay mechanisms, where older entries are re-evaluated or removed if no longer effective.

Additionally, I would include human-in-the-loop validation for high-impact entries. This ensures quality control while still benefiting from automation. The goal is to balance rapid learning with long-term reliability and accuracy.

---

Q3: Handling an Angry Customer Scenario

The system first analyzes the message for intent, sentiment, and context. In this case, the intent is service cancellation, and the sentiment is highly negative.

Step 1: The AI detects strong negative sentiment and repeated complaints, triggering escalation rules.  
Step 2: Instead of providing troubleshooting, the system prioritizes empathy.  
Step 3: The AI responds politely, for example:  
"I'm really sorry for the inconvenience you've experienced. Let me connect you to a specialist right away."  

Step 4: The system escalates the case to a human agent with high priority.  
Step 5: It passes structured context to the agent, including:
- Customer history (multiple previous calls)  
- Issue duration (e.g., 4 days)  
- Intent (service cancellation)  
- Sentiment score (very negative)  

This ensures the agent can quickly understand the situation and respond effectively. The focus is on reducing customer frustration and resolving the issue efficiently.

---

Q4: Most Important System Improvement

The most impactful improvement would be adding a real-time feedback loop for AI responses. After each interaction, the system would collect both explicit feedback (CSAT scores) and implicit signals (escalations, repeated complaints) to continuously improve performance.

This can be implemented by logging all interactions, tagging outcomes, and analyzing patterns where the AI fails or underperforms. Based on this data, the system can adjust prompts, confidence thresholds, or handling strategies for specific intents.

To measure effectiveness, I would track:
- Reduction in escalation rates  
- Improvement in CSAT scores  
- Decrease in repeated complaints  

This creates a self-improving system that adapts to real-world usage. Unlike static systems, it continuously learns from mistakes and becomes more accurate and efficient over time, which is essential for scalability.
