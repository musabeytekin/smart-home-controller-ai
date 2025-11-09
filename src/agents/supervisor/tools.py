from container import container
from langchain.tools import tool
from agents.climate_agent.agent import climate_agent
from agents.security_agent.agent import security_agent
from agents.lighting_agent.agent import lighting_agent


@tool
def manage_climate_system(request: str) -> str:
    """
    Control the homes climate system using natural language.
    Use this when the user wants to modify or check temperatures in specific room/rooms or the entire house.

    Input: Natural language climate control request (e.g., 'set living room
    temperature to 22 degrees', 'what is the temperature in the bedroom?', 'increase the kitchen temperature by 3 degrees', 'increase the temperature by 3 degrees for the entire house')
    """

    result = climate_agent.invoke({
        "messages": [{"role": "user", "content": request}]
    })
    return result["messages"][-1].text


@tool
def get_house_plan() -> str:
    """Get a detailed text-based sketch of the entire house."""
    return container.house.get_house_plan()


@tool
def manage_security(request: str) -> str:
    """
    Control the homes security system using natural language.
    Use this when the user wants to lock/unlock doors.

    Input: Natural language security control request (e.g., 'is the front door locked?', 'lock the back door', 'lock all doors')
    """

    result = security_agent.invoke({
        "messages": [{"role": "user", "content": request}]
    })
    return result["messages"][-1].text

@tool
def manage_lighting(request: str) -> str:
    """
    Control the homes lighting system using natural language.
    Use this when the user wants to modify lighting.

    Input: Natural language lighting control request (e.g., 'turn on the living room lights', 'turn on all lights', 'what is the status of the kitchen lights?')
    """

    result = lighting_agent.invoke({
        "messages": [{"role": "user", "content": request}]
    })
    return result["messages"][-1].text


SUPERVISOR_TOOLKIT = [
    manage_climate_system,
    get_house_plan,
    manage_security,
    manage_lighting,
]

    