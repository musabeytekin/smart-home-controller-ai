from smart_home_controller.src.core.container import container
from .tools import LIGHTNING_TOOLKIT
from langchain.agents import create_agent


__LIGHTNING_AGENT_PROMPT = (
    "You are a smart home lighting assistant. "
    "Control the lighting in the house based on user requests. "
    "House plan details:"
    "\n ------- \n"
    f"{container.house.get_house_plan()}"
    "\n ------- \n"
    "Use the available tools to turn lights on or off in specific rooms or throughout the house. "
    "Always confirm the actions taken in your final response."
)

lightning_agent = create_agent(
    model=container.chat_model,
    tools=LIGHTNING_TOOLKIT,
    system_prompt=__LIGHTNING_AGENT_PROMPT,
)

