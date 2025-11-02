from langchain_core.tools import tool

from smart_home_controller.src.core.models.house import House

@tool
def turn_on_all_lights() -> str:
    """Turn on all lights in the house."""
    # TODO: Implement actual logic to turn on all lights in the house
    return "All lights in the house have been turned on."

@tool
def turn_off_all_lights() -> str:
    """Turn off all lights in the house."""
    # TODO: Implement actual logic to turn off all lights in the house
    return "All lights in the house have been turned off."

@tool
def turn_on_room_light(room_id: str) -> str:
    """Turn on the light in a specific room."""
    # TODO: Implement actual logic to turn on light in specified room
    return f"Light in room {room_id} has been turned on."

@tool
def turn_off_room_light(room_id: str) -> str:
    """Turn off the light in a specific room."""
    # TODO: Implement actual logic to turn off light in specified room
    return f"Light in room {room_id} has been turned off."

@tool 
def turn_off_lights_in_rooms(room_ids: list[str]) -> str:
    """Turn off lights in multiple rooms."""
    # TODO: Implement actual logic to turn off lights in specified rooms
    rooms = ', '.join(room_ids)
    return f"Lights in rooms {rooms} have been turned off."


LIGHTNING_TOOLKIT = [
        turn_on_all_lights,
        turn_off_all_lights,
        turn_on_room_light,
        turn_off_room_light,
        turn_off_lights_in_rooms,
    ]