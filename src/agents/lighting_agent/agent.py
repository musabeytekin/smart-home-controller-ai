from container import container
from .tools import LIGHTING_TOOLKIT
from langchain.agents import create_agent


__LIGHTING_AGENT_PROMPT = (
    "You are a smart home lighting assistant. "
    "Control the lighting in the house based on user requests. "
    "Always get the house sketch using the get_house_sketch tool before performing any actions. "
    "Use the available tools to turn lights on or off in specific rooms or throughout the house. "
    "Always confirm the actions taken in your final response."
)

lighting_agent = create_agent(
    model=container.chat_model,
    tools=LIGHTING_TOOLKIT,
    system_prompt=__LIGHTING_AGENT_PROMPT,
)

