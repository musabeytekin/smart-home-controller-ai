from abc import ABC, abstractmethod



class ClimateService(ABC):

    @abstractmethod
    def set_temperature_all_rooms(self, temperature: float):
        """
        Set the temperature for all rooms in the house.
        
        :raises ValueError: If the temperature is out of acceptable range.
        :raises ConnectionError: If there is an issue connecting to the climate control system.
        """
        pass

    @abstractmethod
    def get_current_temperature(self, room_id: str) -> float:
        """
        Get the current temperature for a specific room.

        :raises ConnectionError: If there is an issue connecting to the climate control system.
        :return: The current temperature of the room.
        """
        pass

    @abstractmethod
    def set_temperature_for_room(self, room_id: str, temperature: float):
        """
        Set the temperature for a specific room.

        :raises ValueError: If the temperature is out of acceptable range.
        :raises ConnectionError: If there is an issue connecting to the climate control system.
        """
        pass

    @abstractmethod
    def increase_temperature(self, room_id: str, increment: float) -> float:
        """
        Increase the temperature for a specific room.

        :raises ValueError: If the temperature is out of acceptable range.
        :raises ConnectionError: If there is an issue connecting to the climate control system.
        :return: The new temperature after increasing.
        """
        pass

    @abstractmethod
    def decrease_temperature(self, room_id: str, decrement: float) -> float:
        """
        Decrease the temperature for a specific room.

        :raises ValueError: If the temperature is out of acceptable range.
        :raises ConnectionError: If there is an issue connecting to the climate control system.
        :return: The new temperature after decreasing.
        """
        pass
