from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.llm_agent import Agent

currency_agent = RemoteA2aAgent(
    name="currency_agent",
    description=(
        "Helpful assistant that can check for currency exchange rates"
    ),
    agent_card=f"http://localhost:8001/{AGENT_CARD_WELL_KNOWN_PATH}",
)

weather_agent = RemoteA2aAgent(
    name="weather_agent",
    description=(
        "Helpful assistant that can check for the weather"
    ),
    agent_card=f"http://localhost:8002/{AGENT_CARD_WELL_KNOWN_PATH}",
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="""
    You are a helpful assistant. Answer user questions to the best of your knowledge
    using the sub agents available
    """,
    sub_agents=[weather_agent, currency_agent]
)
