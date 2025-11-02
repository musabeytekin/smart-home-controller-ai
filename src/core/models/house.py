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