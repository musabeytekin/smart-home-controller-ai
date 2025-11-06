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

    def turn_on_all_lights(self):
        for room in self.rooms:
            room.turn_on_lights()

    def turn_off_all_lights(self):
        for room in self.rooms:
            room.turn_off_lights()
    
    def turn_on_room_light(self, room_id: str):
        for room in self.rooms:
            if room.id == room_id:
                room.turn_on_lights()
                return

    def turn_off_room_light(self, room_id: str):
        for room in self.rooms:
            if room.id == room_id:
                room.turn_off_lights()
                return
            
    def get_all_room_names_list(self) -> list[str]:
        return [room.name for room in self.rooms]
    
    def get_house_plan(self) -> str:
        """
        Returns a detailed text-based sketch of the entire house including:
        - House name
        - Entry door status
        - All rooms with their properties
        - Each room's doors
        """
        plan = []
        plan.append("=" * 60)
        plan.append(f"HOUSE: {self.name}")
        plan.append("=" * 60)
        
        plan.append("\n📍 ENTRY DOOR:")
        plan.append(f"  • Name: {self.entry_door.name}")
        plan.append(f"  • ID: {self.entry_door.id}")
        plan.append(f"  • Status: {'🔒 LOCKED' if self.entry_door.is_locked else '🔓 UNLOCKED'}")
        plan.append(f"  • Lights: {'💡 ON' if self.entry_door.lights_on else '⚫ OFF'}")
        
        plan.append(f"\n🏠 ROOMS ({len(self.rooms)} total):")
        plan.append("-" * 60)
        
        for idx, room in enumerate(self.rooms, 1):
            plan.append(f"\n{idx}. ROOM: {room.name}")
            plan.append(f"   ├─ ID: {room.id}")
            plan.append(f"   ├─ Temperature: {room.temperature}°C")
            plan.append(f"   ├─ Lights: {'💡 ON' if room.light_status else '⚫ OFF'}")
            
            if room.doors:
                plan.append(f"   └─ Doors ({len(room.doors)}):")
                for door_idx, door in enumerate(room.doors, 1):
                    is_last_door = door_idx == len(room.doors)
                    connector = "└─" if is_last_door else "├─"
                    plan.append(f"      {connector} Door {door_idx}: {door.name}")
                    plan.append(f"         • ID: {door.id}")
                    plan.append(f"         • Status: {'🔒 LOCKED' if door.is_locked else '🔓 UNLOCKED'}")
                    plan.append(f"         • Lights: {'💡 ON' if door.lights_on else '⚫ OFF'}")
            else:
                plan.append(f"   └─ Doors: None")
        
        plan.append("\n" + "=" * 60)
        plan.append("END OF HOUSE PLAN")
        plan.append("=" * 60)
        
        return "\n".join(plan)