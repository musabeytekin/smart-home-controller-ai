from abc import ABC, abstractmethod

from core.models.door import Door
from core.models.house import House


class SecurityService(ABC):

    def __init__(self, house: House):
        self.house = house

    @abstractmethod
    def lock_entry_door(self) -> Door:
        """
        Lock the main entry door of the house.
        :raises SecurityError: If there is an issue with the security system.
        :raises DoorNotFoundError: If the entry door is not found.
        :return: The locked Door details.
        """
        pass

    @abstractmethod
    def unlock_entry_door(self) -> Door:
        """
        Unlock the main entry door of the house.
        :raises SecurityError: If there is an issue with the security system.
        :raises DoorNotFoundError: If the entry door is not found.
        :return: The unlocked Door details.
        """
        pass

    @abstractmethod
    def lock_door(self, door_id: str) -> Door:
        """
        Lock a specific door in the house.

        :param door_id: The ID of the door to lock.
        :raises SecurityError: If there is an issue with the security system.
        :raises DoorNotFoundError: If the specified door is not found.
        :return: The locked Door details.
        """
        pass

    @abstractmethod
    def lock_doors(self, door_ids: list[str]) -> list[Door]:
        """
        Lock multiple specific doors in the house.

        :param door_ids: The IDs of the doors to lock.
        :raises SecurityError: If there is an issue with the security system.
        :raises DoorNotFoundError: If any of the specified doors are not found.
        :return: A list of locked Door details.
        """
        pass

    @abstractmethod
    def unlock_door(self, door_id: str) -> Door:
        """
        Unlock a specific door in the house.

        :param door_id: The ID of the door to unlock.
        :raises SecurityError: If there is an issue with the security system.
        :raises DoorNotFoundError: If the specified door is not found.
        :return: The unlocked Door details.
        """
        pass

    @abstractmethod
    def unlock_doors(self, door_ids: list[str]) -> list[Door]:
        """
        Unlock multiple specific doors in the house.

        :param door_ids: The IDs of the doors to unlock.
        :raises SecurityError: If there is an issue with the security system.
        :raises DoorNotFoundError: If any of the specified doors are not found.
        :return: A list of unlocked Door details.
        """
        pass

    @abstractmethod
    def lock_all_doors(self):
        """
        Lock all doors in the house.

        :raises SecurityError: If there is an issue with the security system.
        """
        pass

    @abstractmethod
    def unlock_all_doors(self):
        """
        Unlock all doors in the house.

        :raises SecurityError: If there is an issue with the security system.
        """
        pass

    @abstractmethod
    def lock_room_doors(self, room_id: str) -> list[Door]:
        """
        Lock all doors in a specific room.

        :param room_id: The ID of the room.
        :raises SecurityError: If there is an issue with the security system.
        :return: A list of locked Door details in the specified room.
        """
        pass

    @abstractmethod
    def lock_rooms_doors(self, room_ids: list[str]) -> list[Door]:
        """
        Lock all doors in specific rooms.

        :param room_ids: The IDs of the rooms.
        :raises SecurityError: If there is an issue with the security system.
        :return: A list of locked Door details in the specified rooms.
        """
        pass

    @abstractmethod
    def unlock_room_doors(self, room_id: str) -> list[Door]:
        """
        Unlock all doors in a specific room.

        :param room_id: The ID of the room.
        :raises SecurityError: If there is an issue with the security system.
        :return: A list of unlocked Door details in the specified room.
        """
        pass

    @abstractmethod
    def unlock_rooms_doors(self, room_ids: list[str]) -> list[Door]:
        """
        Unlock all doors in specific rooms.

        :param room_ids: The IDs of the rooms.
        :raises SecurityError: If there is an issue with the security system.
        :return: A list of unlocked Door details in the specified rooms.
        """
        pass
