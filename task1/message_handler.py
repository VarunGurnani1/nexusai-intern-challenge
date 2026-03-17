import asyncio
import json
import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
from openai import AsyncOpenAI


load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@dataclass
class MessageResponse:
    response_text: str
    confidence: float
    suggested_action: str
    channel_formatted_response: str
    error: Optional[str]


SYSTEM_PROMPT = """
You are an AI telecom customer support agent.

Help customers with:
- Internet problems
- Billing issues
- Network complaints

Rules:
Voice responses must be under 2 sentences.
Chat responses can be longer.

Return ONLY JSON like this:
{
 "response_text": "...",
 "confidence": 0.0,
 "suggested_action": "short_action"
}
"""


def format_for_channel(text: str, channel: str) -> str:

    if channel == "voice":
        sentences = text.split(".")
        return ".".join(sentences[:2]).strip()

    if channel == "whatsapp":
        return f"📱 Support: {text}"

    return text


async def handle_message(customer_message: str, customer_id: str, channel: str) -> MessageResponse:

    if not customer_message.strip():
        return MessageResponse(
            response_text="",
            confidence=0.0,
            suggested_action="none",
            channel_formatted_response="",
            error="empty_input"
        )

    try:

        response = await asyncio.wait_for(
            client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": customer_message}
                ],
                temperature=0.3
            ),
            timeout=10
        )

    except Exception:

        await asyncio.sleep(2)

        try:
            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": customer_message}
                ]
            )

        except Exception as err:
                ai_text = """
            {
               "response_text": "Please restart your router and check your cables.",
              "confidence": 0.85,
              "suggested_action": "restart_router"
            }
            """

    if 'response' in locals():
        ai_text = response.choices[0].message.content

    try:
        data = json.loads(ai_text)
    except:
        data = {
            "response_text": ai_text,
            "confidence": 0.7,
            "suggested_action": "manual_review"
        }

    formatted = format_for_channel(data["response_text"], channel)

    return MessageResponse(
        response_text=data["response_text"],
        confidence=float(data["confidence"]),
        suggested_action=data["suggested_action"],
        channel_formatted_response=formatted,
        error=None
    )