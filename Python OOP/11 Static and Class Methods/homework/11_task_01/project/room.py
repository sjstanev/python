class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests: int = 0
        self.is_taken: bool = False


    def take_room(self, people: int) -> str:
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"
        # self.capacity -= people
        self.guests = people
        self.is_taken = True


    def free_room(self) -> str:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0

    def __repr__(self) -> str:
        return f"self.number {self.number}, self.capacity {self.capacity}, self.guest: {self.guest}, is_taken: {self.is_taken}"