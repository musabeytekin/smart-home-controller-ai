class Door:
    def __init__(self, id: str, name: str, is_locked: bool, lights_on: bool = False):
        self.id = id
        self.name = name
        self.is_locked = is_locked
        self.lights_on = lights_on
    
    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

    def turn_lights_on(self):
        self.lights_on = True
    
    def turn_lights_off(self):
        self.lights_on = False