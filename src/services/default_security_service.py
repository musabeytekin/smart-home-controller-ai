import re
from core.models.door import Door
from core.models.house import House
from core.security_service import SecurityService
from core.exception.security_error import SecurityError
from core.exception.door_not_found_error import DoorNotFoundError


class DefaultSecurityService(SecurityService):

    def lock_entry_door(self) -> Door:
        try:
            if not self.house.entry_door:
                raise DoorNotFoundError("Entry door not found in the house.")

            self.house.entry_door.lock()
            return self.house.entry_door
        except AttributeError as e:
            raise SecurityError(f"Failed to lock entry door: {str(e)}")

    def unlock_entry_door(self) -> Door:
        try:
            if not self.house.entry_door:
                raise DoorNotFoundError("Entry door not found in the house.")

            self.house.entry_door.unlock()
            return self.house.entry_door
        except AttributeError as e:
            raise SecurityError(f"Failed to unlock entry door: {str(e)}")

    def lock_door(self, door_id: str) -> Door:
        try:
            if self.house.entry_door.id == door_id:
                self.house.entry_door.lock()
                return self.house.entry_door

            door = self.house.get_door_by_id(door_id)
            if door:
                door.lock()
            else:
                raise DoorNotFoundError(
                    f"Door with ID '{door_id}' not found in the house.")

            return door

        except DoorNotFoundError:
            raise
        except Exception as e:
            raise SecurityError(f"Failed to lock door '{door_id}': {str(e)}")

    def lock_doors(self, door_ids: list[str]) -> list[Door]:
        locked_doors = []

        for door_id in door_ids:
            locked_door = self.lock_door(door_id)
            locked_doors.append(locked_door)

        return locked_doors

    def unlock_door(self, door_id: str) -> Door:
        try:
            door = self.house.get_door_by_id(door_id)
            if door:
                door.unlock()
            else:
                raise DoorNotFoundError(
                    f"Door with ID '{door_id}' not found in the house.")

            return door

        except DoorNotFoundError:
            raise
        except Exception as e:
            raise SecurityError(f"Failed to unlock door '{door_id}': {str(e)}")

    def unlock_doors(self, door_ids: list[str]) -> list[Door]:
        unlocked_doors = []

        for door_id in door_ids:
            unlocked_door = self.unlock_door(door_id)
            unlocked_doors.append(unlocked_door)

        return unlocked_doors

    def lock_all_doors(self) -> list[Door]:
        try:
            locked_doors = []

            for door in self.house.get_all_doors():
                door.lock()
                locked_doors.append(door)

            return locked_doors
        except Exception as e:
            raise SecurityError(f"Failed to lock all doors: {str(e)}")

    def unlock_all_doors(self) -> list[Door]:

        try:
            unlocked_doors = []

            for door in self.house.get_all_doors():
                door.unlock()
                unlocked_doors.append(door)

            return unlocked_doors
        except Exception as e:
            raise SecurityError(f"Failed to unlock all doors: {str(e)}")

    def lock_room_doors(self, room_id: str) -> list[Door]:

        try:
            room = self.house.get_room_by_id(room_id)
            locked_doors = []

            for door in room.doors:
                door.lock()
                locked_doors.append(door)

            return locked_doors
        
        except Exception as e:
            raise SecurityError(
                f"Failed to lock doors in room '{room_id}': {str(e)}")

    def lock_rooms_doors(self, room_ids: list[str]) -> list[Door]:
        locked_doors = []

        for room_id in room_ids:
            doors = self.lock_room_doors(room_id)
            locked_doors.extend(doors)

        return locked_doors

    def unlock_room_doors(self, room_id: str) -> list[Door]:
        try:
            room = self.house.get_room_by_id(room_id)
            unlocked_doors = []

            for door in room.doors:
                door.unlock()
                unlocked_doors.append(door)

            return unlocked_doors
        except Exception as e:
            raise SecurityError(
                f"Failed to unlock doors in room '{room_id}': {str(e)}")

    def unlock_rooms_doors(self, room_ids: list[str]) -> list[Door]:

        unlocked_doors = []

        for room_id in room_ids:
            doors = self.unlock_room_doors(room_id)
            unlocked_doors.extend(doors)

        return unlocked_doors
