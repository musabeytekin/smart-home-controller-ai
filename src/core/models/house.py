from core.exception.door_not_found_error import DoorNotFoundError
from .door import Door
from .room import Room


class House:
    def __init__(self, name: str, rooms: list[Room], entry_door: Door):
        self.name = name
        self.rooms = rooms
        self.entry_door = entry_door

    
    def lock_entry(self):
        self.entry_door.lock()

    def unlock_entry(self):
        self.entry_door.unlock()

    def turn_on_all_lights(self):
        for room in self.rooms:
            room.turn_on_lights()

    def turn_off_all_lights(self):
        for room in self.rooms:
            room.turn_off_lights()
    
    def turn_on_room_light(self, room_id: str):
        for room in self.rooms:
            if room.id == room_id:
                room.turn_on_lights()
                return

    def turn_off_room_light(self, room_id: str):
        for room in self.rooms:
            if room.id == room_id:
                room.turn_off_lights()
                return
            
    def get_all_room_names_list(self) -> list[str]:
        return [room.name for room in self.rooms]
    
    def get_house_plan(self) -> str:
        """
        Returns a concise text-based representation of the house for LLM prompts.
        Includes essential information: house name, entry door, rooms, and their properties.
        """
        plan = [f"House: {self.name}"]
        
        plan.append(f"Entry Door: {self.entry_door.name} (ID: {self.entry_door.id}, {'Locked' if self.entry_door.is_locked else 'Unlocked'})")
        
        plan.append(f"Rooms ({len(self.rooms)}):")
        for room in self.rooms:
            plan.append(f"  - {room.name} (ID: {room.id}, Temp: {room.temperature}°C, Lights: {'On' if room.light_status else 'Off'})")
            
            if room.doors:
                for door in room.doors:
                    plan.append(f"    - Door: {door.name} (ID: {door.id}, {'Locked' if door.is_locked else 'Unlocked'})")
        
        return "\n".join(plan)
    
    
    def get_room_by_id(self, room_id: str) -> Room:
        for room in self.rooms:
            if room.id == room_id:
                return room
        raise ValueError(f"Room with ID {room_id} not found.")
    
    
    def get_door_by_id(self, door_id: str) -> Door:
        for door in self.get_all_doors():
            if door.id == door_id:
                return door
        
        raise DoorNotFoundError(f"Door with ID {door_id} not found.")
    
    
    def get_all_doors(self) -> list[Door]:
        seen_ids = {self.entry_door.id}
        doors = [self.entry_door]
        
        for room in self.rooms:
            for door in room.doors:
                if door.id not in seen_ids:
                    doors.append(door)
                    seen_ids.add(door.id)
        
        return doors

