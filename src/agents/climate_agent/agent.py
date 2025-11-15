from container import container
from .tools import CLIMATE_TOOLKIT
from langchain.agents import create_agent


__CLIMATE_AGENT_PROMPT = (
    "You are a smart home climate control assistant. "
    "Manage the temperature settings in the house based on user requests. "
    "Always get the house sketch using the get_house_sketch tool before performing any actions. "
    "Use the available tools to set, increase, or decrease temperatures in specific rooms or throughout the house. "
    "Always confirm the actions taken in your final response."
)

climate_agent = create_agent(
    model=container.chat_model,
    tools=CLIMATE_TOOLKIT,
    system_prompt=__CLIMATE_AGENT_PROMPT,
)