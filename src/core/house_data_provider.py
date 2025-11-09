from core.models.door import Door
from core.models.room import Room
from core.models.house import House

def __get_fresh_house() -> House:
    """Create and return a fresh House instance with default data."""
    entry_door = Door(
        id="entry_door",
        name="Entry Door",
        is_locked=True,
    )
    entree_to_sitting_room_door = Door(
        id="entree_to_sitting_room_door",
        name="Entree to Sitting Room Door",
        is_locked=False,
    )

    small_entrance_hall_to_entree_door = Door(
        id="small_entrance_hall_to_entree_door",
        name="Small Entrance Hall to Entree Door",
        is_locked=False,
    )
    entree_to_kitchen_door = Door(
        id="entree_to_kitchen_door",
        name="Entree to Kitchen Door",
        is_locked=False,
    )

    entree_to_living_room_door = Door(
        id="entree_to_living_room_door",
        name="Entree to Living Room Door",
        is_locked=False,
    )

    entree_to_nursery_door = Door(
        id="entree_to_nursery_door",
        name="Entree to Nursery Door",
        is_locked=False,
    )

    small_entrance_hall_to_bedroom_door = Door(
        id="small_entrance_hall_to_bedroom_door",
        name="Small Entrance Hall to Bedroom Door",
        is_locked=False,
    )

    kitchen: Room = Room(
        id="kitchen",
        name="Kitchen",
        doors=[entree_to_kitchen_door],
        light_status=False,
        temperature=22.0,
    )

    living_room: Room = Room(
        id="living_room",
        name="Living Room",
        doors=[entree_to_living_room_door],
        light_status=False,
        temperature=22.0,
    )

    nursery: Room = Room(
        id="nursery",
        name="Nursery",
        doors=[entree_to_nursery_door],
        light_status=False,
        temperature=22.0,
    )

    bedroom: Room = Room(
        id="bedroom",
        name="Bedroom",
        doors=[small_entrance_hall_to_bedroom_door],
        light_status=False,
        temperature=22.0,
    )

    entree: Room = Room(
        id="entree",
        name="Entree",
        doors=[
            entree_to_sitting_room_door,
            small_entrance_hall_to_entree_door,
            entree_to_kitchen_door,
            entree_to_living_room_door,
            entree_to_nursery_door,
        ],
        light_status=False,
        temperature=22.0,
    )

    small_entrance_hall: Room = Room(
        id="small_entrance_hall",
        name="Small Entrance Hall",
        doors=[small_entrance_hall_to_bedroom_door, small_entrance_hall_to_entree_door],
        light_status=False,
        temperature=22.0,
    )

    sitting_room: Room = Room(
        id="sitting_room",
        name="Sitting Room",
        doors=[entree_to_sitting_room_door],
        light_status=False,
        temperature=22.0,
    )

    house = House(
        "Musa's Smart Home",
        rooms=[
            kitchen,
            living_room,
            nursery,
            bedroom,
            entree,
            small_entrance_hall,
            sitting_room,
        ],
        entry_door=entry_door,
    )

    return house





    

house = __get_fresh_house()


def get_house() -> House:
    """Retrieve the current house data."""
    return house


