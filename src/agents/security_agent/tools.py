from langchain_core.tools import tool
from container import container
from core import security_service
from core.models.house import House

@tool
def get_house_sketch() -> str:
    """Get a detailed text-based sketch of the entire house."""
    house = container.house
    return house.get_house_plan()


@tool
def lock_entry_door() -> str:
    """Lock the main entry door of the house."""
    security_service = container.security_service
    door = security_service.lock_entry_door()
    return f"Entry door '{door.name}' has been locked."

@tool
def unlock_entry_door() -> str:
    """Unlock the main entry door of the house."""
    security_service = container.security_service
    door = security_service.unlock_entry_door()
    return f"Entry door '{door.name}' has been unlocked."

@tool
def lock_door(door_id: str) -> str:
    """Lock a specific door in the house."""
    security_service = container.security_service
    door = security_service.lock_door(door_id)
    return f"Door '{door.name}' has been locked."

@tool
def unlock_door(door_id: str) -> str:
    """Unlock a specific door in the house."""
    security_service = container.security_service
    door = security_service.unlock_door(door_id)
    return f"Door '{door.name}' has been unlocked."

@tool
def lock_doors(door_ids: list[str]) -> str:
    """Lock multiple specific doors in the house."""
    security_service = container.security_service
    doors = security_service.lock_doors(door_ids)
    door_names = ', '.join([door.name for door in doors])
    return f"Doors '{door_names}' have been locked."

@tool
def unlock_doors(door_ids: list[str]) -> str:
    """Unlock multiple specific doors in the house."""
    security_service = container.security_service
    doors = security_service.unlock_doors(door_ids)
    door_names = ', '.join([door.name for door in doors])
    return f"Doors '{door_names}' have been unlocked."


@tool
def lock_all_doors() -> str:
    """Lock all doors in the house."""
    security_service = container.security_service
    security_service.lock_all_doors()
    return f"All doors have been locked."

@tool
def unlock_all_doors() -> str:
    """Unlock all doors in the house."""
    security_service = container.security_service
    security_service.unlock_all_doors()
    return f"All doors have been unlocked."


@tool
def lock_room_doors(room_id: str) -> str:
    """Lock all doors in a specific room."""
    security_service = container.security_service
    doors_locked = security_service.lock_room_doors(room_id)
    door_names = ', '.join([door.name for door in doors_locked])
    return f"All doors in room '{room_id}' have been locked: {door_names}."

@tool
def unlock_room_doors(room_id: str) -> str:
    """Unlock all doors in a specific room."""
    security_service = container.security_service
    doors_unlocked = security_service.unlock_room_doors(room_id)
    door_names = ', '.join([door.name for door in doors_unlocked])
    return f"All doors in room '{room_id}' have been unlocked: {door_names}."

@tool
def lock_rooms_doors(room_ids: list[str]) -> str:
    """Lock all doors in multiple specific rooms."""
    security_service = container.security_service
    doors_locked = security_service.lock_rooms_doors(room_ids)
    door_names = ', '.join([door.name for door in doors_locked])
    return f"All doors in rooms '{', '.join(room_ids)}' have been locked: {door_names}."


@tool
def unlock_rooms_doors(room_ids: list[str]) -> str:
    """Unlock all doors in multiple specific rooms."""
    security_service = container.security_service
    doors_unlocked = security_service.unlock_rooms_doors(room_ids)
    door_names = ', '.join([door.name for door in doors_unlocked])
    return f"All doors in rooms '{', '.join(room_ids)}' have been unlocked: {door_names}."



SECURITY_TOOLKIT = [
    get_house_sketch,
    lock_entry_door,
    unlock_entry_door,
    lock_door,
    unlock_door,
    lock_doors,
    unlock_doors,
    lock_all_doors,
    unlock_all_doors,
    lock_room_doors,
    unlock_room_doors,
    lock_rooms_doors,
    unlock_rooms_doors,
]