from langchain_core.tools import tool
from core.container import container
from core.models.house import House

@tool
def get_house_sketch() -> str:
    """Get a detailed text-based sketch of the entire house."""
    house: House = container.house
    return house.get_house_plan()


@tool
def set_temperature_all_rooms(temperature: float) -> str:
    """Set the temperature for all rooms in the house."""
    climate_service = container.climate_service
    climate_service.set_temperature_all_rooms(temperature)
    return f"Temperature for all rooms has been set to {temperature}°C."


@tool
def get_current_temperature(room_id: str) -> float:
    """Get the current temperature for a specific room."""
    climate_service = container.climate_service
    return climate_service.get_current_temperature(room_id)


@tool
def set_temperature_for_room(room_id: str, temperature: float) -> str:
    """Set the temperature for a specific room."""
    climate_service = container.climate_service
    climate_service.set_temperature_for_room(room_id, temperature)
    room_name = container.house.get_room_by_id(room_id).name
    return f"Temperature for room {room_name} has been set to {temperature}°C."


@tool
def increase_temperature(room_id: str, increment: float) -> float:
    """
    Increase the temperature for a specific room.
    Returns the new temperature after increasing.
    """
    climate_service = container.climate_service
    return climate_service.increase_temperature(room_id, increment)


@tool
def decrease_temperature(room_id: str, decrement: float) -> float:
    """Decrease the temperature for a specific room."""
    climate_service = container.climate_service
    return climate_service.decrease_temperature(room_id, decrement)


CLIMATE_TOOLKIT = [
    get_house_sketch,
    set_temperature_all_rooms,
    get_current_temperature,
    set_temperature_for_room,
    increase_temperature,
    decrease_temperature,
]