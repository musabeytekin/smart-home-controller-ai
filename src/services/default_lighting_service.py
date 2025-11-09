from core.models import room
from core.models.house import House
from core.lighting_service import LightingService


class DefaultLightingService(LightingService):

    def turn_on_all_lights(self):
        self.house.turn_on_all_lights()

    def turn_off_all_lights(self) -> str:
        self.house.turn_off_all_lights()
        room_names = self.house.get_all_room_names_list()
        rooms = ', '.join(room_names)
        return f"All lights have been turned off in the following rooms: {rooms}."

    def turn_on_room_light(self, room_id: str):
        self.house.turn_on_room_light(room_id)

    def turn_off_room_light(self, room_id: str):
        self.house.turn_off_room_light(room_id)

    def turn_off_lights_in_rooms(self, room_ids: list[str]):
        for room_id in room_ids:
            self.house.turn_off_room_light(room_id)



