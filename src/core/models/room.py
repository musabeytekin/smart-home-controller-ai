from .door import Door

class Room:
    def __init__(self, id: str, name: str, temperature: float, light_status: bool, doors: list[Door]):
        self.id = id
        self.name = name
        self.temperature = temperature
        self.light_status = light_status
        self.doors = doors