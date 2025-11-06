from langchain_core.tools import tool
from core.models.house import House
from core.container import container

@tool
def turn_on_all_lights() -> str:
    """Turn on all lights in the house."""
    return container.lightning_service.turn_on_all_lights()


@tool
def turn_off_all_lights() -> str:
    """Turn off all lights in the house."""
    return container.lightning_service.turn_off_all_lights()

@tool
def turn_on_room_light(room_id: str) -> str:
    """Turn on the light in a specific room."""
    return container.lightning_service.turn_on_room_light(room_id)  

@tool
def turn_off_room_light(room_id: str) -> str:
    """Turn off the light in a specific room."""
    return container.lightning_service.turn_off_room_light(room_id)

@tool 
def turn_off_lights_in_rooms(room_ids: list[str]) -> str:
    """Turn off lights in multiple rooms."""
    return container.lightning_service.turn_off_lights_in_rooms(room_ids)

@tool
def get_house_sketch() -> str:
    """Get a detailed text-based sketch of the entire house."""
    house: House = container.house
    return house.get_house_plan()

LIGHTNING_TOOLKIT = [
        turn_on_all_lights,
        turn_off_all_lights,
        turn_on_room_light,
        turn_off_room_light,
        turn_off_lights_in_rooms,
        get_house_sketch,
    ]