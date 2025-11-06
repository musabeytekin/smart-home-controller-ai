from core.models import room
from core.models.house import House
from core.climate_service import ClimateService
from core.container import container


class DefaultClimateService(ClimateService):


    def set_temperature_all_rooms(self, temperature: float):
        for room in self.house.rooms:
            room.temperature = temperature

    def get_current_temperature(self, room_id: str) -> float:
        room = self.house.get_room_by_id(room_id)
        return room.temperature

    def set_temperature_for_room(self, room_id: str, temperature: float):
        room = self.house.get_room_by_id(room_id)
        room.temperature = temperature

    def increase_temperature(self, room_id: str, increment: float) -> float:
        room = self.house.get_room_by_id(room_id)
        room.temperature += increment
        return room.temperature

    def decrease_temperature(self, room_id: str, decrement: float) -> float:
        room = self.house.get_room_by_id(room_id)
        room.temperature -= decrement
        return room.temperature