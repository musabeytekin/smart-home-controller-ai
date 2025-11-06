from langchain_core.tools import tool
from core.container import container
from core.models.house import House

@tool
def get_house_sketch() -> str:
    """Get a detailed text-based sketch of the entire house."""
    house = container.house
    return house.get_house_plan()