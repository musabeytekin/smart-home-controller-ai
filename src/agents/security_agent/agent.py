from container import container
from .tools import SECURITY_TOOLKIT
from langchain.agents import create_agent

__SECURITY_AGENT_PROMPT = (
    "You are a smart home security assistant. "
    "Manage the locking and unlocking of doors in the house based on user requests. "
    "House plan details:"
    "\n ------- \n"
    f"{container.house.get_house_plan()}"
    "\n ------- \n"
    "Use the available tools to lock or unlock specific doors or all doors in the house. "
    "Always confirm the actions taken in your final response."
)

security_agent = create_agent(
    model=container.chat_model,
    tools=SECURITY_TOOLKIT,
    system_prompt=__SECURITY_AGENT_PROMPT,
)
