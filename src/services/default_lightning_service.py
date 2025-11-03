from smart_home_controller.src.core.models import room
from smart_home_controller.src.core.models.house import House
from smart_home_controller.src.core.lightning_service import LightningService
from smart_home_controller.src.core.container import container


class DefaultLightningService(LightningService):
    def __init__(self, house: House):
        self.house = house

    def turn_on_all_lights(self) -> str:
        self.house.turn_on_all_lights()
        room_names = self.house.get_all_room_names_list()
        rooms = ', '.join(room_names)
        return f"All lights have been turned on in the following rooms: {rooms}."

    def turn_off_all_lights(self) -> str:
        self.house.turn_off_all_lights()
        room_names = self.house.get_all_room_names_list()
        rooms = ', '.join(room_names)
        return f"All lights have been turned off in the following rooms: {rooms}."

    def turn_on_room_light(self, room_id: str) -> str:
        self.house.turn_on_room_light(room_id)
        return f"Light in room {room_id} has been turned on."

    def turn_off_room_light(self, room_id: str) -> str:
        self.house.turn_off_room_light(room_id)
        return f"Light in room {room_id} has been turned off."

    def turn_off_lights_in_rooms(self, room_ids: list[str]) -> str:
        for room_id in room_ids:
            self.house.turn_off_room_light(room_id)
        rooms = ', '.join(room_ids)
        return f"Lights in rooms {rooms} have been turned off."


