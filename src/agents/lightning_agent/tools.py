from langchain_core.tools import tool
from core.models.house import House
from core.container import container

@tool
def turn_on_all_lights() -> str:
    """Turn on all lights in the house."""
    container.lightning_service.turn_on_all_lights()
    return "All lights have been turned on."


@tool
def turn_off_all_lights() -> str:
    """Turn off all lights in the house."""
    container.lightning_service.turn_off_all_lights()
    return "All lights have been turned off."

@tool
def turn_on_room_light(room_id: str) -> str:
    """Turn on the light in a specific room."""
    container.lightning_service.turn_on_room_light(room_id)
    room_name = container.house.get_room_by_id(room_id).name
    return f"Light in room {room_name} has been turned on."

@tool
def turn_off_room_light(room_id: str) -> str:
    """Turn off the light in a specific room."""
    container.lightning_service.turn_off_room_light(room_id)
    room_name = container.house.get_room_by_id(room_id).name
    return f"Light in room {room_name} has been turned off."

@tool 
def turn_off_lights_in_rooms(room_ids: list[str]) -> str:
    """Turn off lights in multiple rooms."""
    container.lightning_service.turn_off_lights_in_rooms(room_ids)
    return f"Lights in rooms {', '.join(container.house.get_room_by_id(room_id).name for room_id in room_ids)} have been turned off."

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