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
       # TODO: Implement a method to return a string representation of the house plan
       return ''