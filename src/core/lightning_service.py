from abc import ABC, abstractmethod

from core.models.house import House

class LightningService(ABC):

    def __init__(self, house: House):
        self.house = house

    @abstractmethod
    def turn_on_all_lights(self):
        """
        Turn on all lights in the house.

        :raises LightingError: If there is an issue with the lighting system.
        """
        pass

    @abstractmethod
    def turn_off_all_lights(self):
        """
        Turn off all lights in the house.
        :raises LightingError: If there is an issue with the lighting system.
        """
        pass

    @abstractmethod
    def turn_on_room_light(self, room_id: str):
        """
        Turn on the light in a specific room.

        :param room_id: The ID of the room.
        :raises LightingError: If there is an issue with the lighting system.
        """
        pass

    @abstractmethod
    def turn_off_room_light(self, room_id: str):
        """
        Turn off the light in a specific room.

        :param room_id: The ID of the room.
        :raises LightingError: If there is an issue with the lighting system.
        """
        pass

    @abstractmethod
    def turn_off_lights_in_rooms(self, room_ids: list[str]):
        """
        Turn off the lights in specific rooms.

        :param room_ids: The IDs of the rooms.
        :raises LightingError: If there is an issue with the lighting system.
        """
        pass
