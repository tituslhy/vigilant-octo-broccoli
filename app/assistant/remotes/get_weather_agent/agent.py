from google.adk.agents.llm_agent import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.lite_llm import LiteLlm

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

llm = LiteLlm(
    model="ollama_chat/gpt-oss:20b",
    temperature=0,
)

def get_weather(location: str):
    """Use this tool to get the weather of a given location"""
    return f"The weather is sunny in {location}."

root_agent = Agent(
    model=llm,
    # model='gemini-2.5-flash',
    name='weather_agent',
    description='You are a helpful assistant for user questions relating to weather.',
    instruction='Answer user questions to the best of your knowledge using tools',
    tools = [get_weather]
)

a2a_weather_app = to_a2a(root_agent, port=8002)