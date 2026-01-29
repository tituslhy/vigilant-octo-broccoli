from google.adk.agents.llm_agent import Agent

import httpx
from typing import Annotated
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.lite_llm import LiteLlm

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

llm = LiteLlm(
    model="ollama_chat/gpt-oss:20b",
    temperature=0,
)

async def get_exchange_rates(
    currency_from: Annotated[str, "Currency to exchange from. For e.g. USD"],
    currency_to: Annotated[str, "Currency to exchange to. For e.g. EUR"]
):
    """
    Use this tool to get exchange rates between two currencies.
    
    Args:
        currency_from: The currency to convert from (e.g., "USD").
        currency_to: The currency to convert to (e.g., "EUR").

    Returns:
        A dictionary containing the exchange rate data, or an error message if the request fails.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.frankfurter.app/latest",
                params={"from": currency_from, "to": currency_to},
            )
            response.raise_for_status()

            data = response.json()
            if "rates" not in data:
                return {"error": "Invalid API response format."}
            return data
    except httpx.HTTPError as e:
        return {"error": f"API request failed: {e}"}
    except ValueError:
        return {"error": "Invalid JSON response from API."}
    
root_agent = Agent(
    model = llm,
    # model='gemini-2.5-flash',
    name='currency_exchange_agent',
    description='You are a helpful assistant for user questions relating to exchange rates.',
    instruction='Answer user questions to the best of your knowledge using tools',
    tools = [get_exchange_rates],
)

a2a_currency_app = to_a2a(root_agent, port=8001)