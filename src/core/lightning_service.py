from abc import ABC, abstractmethod

class LightningService(ABC):

    @abstractmethod
    def turn_on_all_lights(self) -> str:
        pass

    @abstractmethod
    def turn_off_all_lights(self) -> str:
        pass

    @abstractmethod
    def turn_on_room_light(self, room_id: str) -> str:
        pass

    @abstractmethod
    def turn_off_room_light(self, room_id: str) -> str:
        pass

    @abstractmethod
    def turn_off_lights_in_rooms(self, room_ids: list[str]) -> str:
        pass
