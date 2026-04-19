"""Optional OpenAI commentary on a trading signal."""
import os

from openai import OpenAI


def commentary(symbol: str, action: str, last_price: float) -> str | None:
    """Return a one-sentence commentary, or None if OPENAI_API_KEY is unset."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": (
                f"One short sentence: {symbol} just produced a '{action}' signal "
                f"at {last_price}. What's the takeaway for a trader?"
            ),
        }],
    )
    return response.choices[0].message.content.strip()
