
class Person:
    def __init__ (self, name: str) -> None:
        self.name = name

person = Person('Peter')
print(setattr(person, 'name', 'George'))    # None
print(person.name)                          # George   
print(setattr(person, 'age', '21'))         # None
print(person.age)                           # 21