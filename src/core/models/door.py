class Door:
    def __init__(self, id: str, is_locked: bool):
        self.id = id
        self.is_locked = is_locked
    
    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

