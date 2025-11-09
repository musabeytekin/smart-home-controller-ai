from container import container
from .tools import SUPERVISOR_TOOLKIT
from langchain.agents import create_agent


__SUPERVISOR_AGENT_PROMPT = (
    "You are a smart home assistant. "
    "You can manage the home's climate, security, and lighting systems based on user requests. "
    "Break down user requests into appropriate tool calls and coordinate the results. "
    "When a request involves multiple actions, use multiple tools in sequence."
)

supervisor_agent = create_agent(
    model=container.chat_model,
    tools=SUPERVISOR_TOOLKIT,
    system_prompt=__SUPERVISOR_AGENT_PROMPT,
)
