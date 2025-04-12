# Polymorphism and Abstraction
## Having Multiple Forms

- [What is Polymorphism](#what-is-polymorphism)
- [Overloading Built-in Methods](#overloading-built-in-methods)
- [Duck Typing](#duck-typing)
- [What is Abstraction](#what-is-abstraction)

## What is Polymorphism
### Polymorphism Definition
- Polymorphism is based on the the Greek word "poly" (**many**) and "morphism" (**forms**)
- It is ability to present the **same interface** (methods) for **differing underlying forms** through the interface of
**their base class**
- e.g., **Square**, and **Triangle inherit Shape**, so their instance can be used from en interface of type Shape
### Run-Time Polymorphism
- A subclass can **override** a method of its superclass
  - e.g., **both** triangle and square are **shapes** and have **area**
```python
A = b.h/2 (triangle)    A = s**2 (square)
```
```python
class Shape:
    def get_area(self):
        return None

class Square:
    side: int = 2
    def get_area(self) -> int:
        return self.side * self.side

class Triangle:
    base: int = 4
    height: int = 2
    def get_area(self) -> float:
        return 0.5 * self.base * self.height
```
### Without Polymorphism
- A **type check** may be required before performing an action on an object to **determine the correct method** to call
```python
class Square:
    side: int = 2
    def calculate_square_area(self) -> int:
        return self.side * self.side

class Triangle:
    base: int = 4
    height: int = 2
    def calculate_triangle_area(self) -> float:
        return 0.5 * self.base * self.height
    
for obj in Square(), Triangle():
    if isinstance(obj, Square):
        area = obj.calculate_square_area()
    elif isinstance(obj, Triangle):
        area = obj.calculate_triangle_area()
    print(area)
```
### Compile-Time Polymorphism
- Python **does not** support compile-time polymorphism or **method overloading**
- If a class has multiple methods **with the same name**, the method define in the **last will override** the earlier one
```python
class Person:
    def say_hello() -> str:
        return 'Hi!'

    def say_hello() -> str:
        return "Hello!"

print(Person.say_hello())   # Hello!
```
## Overloading Built-in Methods
- **Change the behavior** of functions such `len`, `abs`, `str`, `repr`, and so on
- To do this only meed to define the corresponding **special method in your class**
```python
class MyClass:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __len__(self):
        return self.size

my_class = MyClass("Class Name", 3)
print(len(my_class))    # 3
```
### Operator Overriding/Overloading
- An operator behaves **differently** based on the **type of the operands**
- e.g., operator "+" is used to add two **integers** as well to join two **strings** and merge two **list**
- It is override by `int` class, `str` class and `list` class
```python
integer = 1 + 1
string = "Hello " + "Jerry"
list = ["1", "2"] + ["3", "4"]
```

| Magic Methods               | Get Classed Using |
|-----------------------------|-------------------|
| `__and__`(self, other)      | +                 |
| `__sub__`(self, other)      | -                 |
| `__mul__`(self, other)      | *                 |
| `__floordiv__`(self, other) | //                |
| `__truediv__`(self, other)  | /                 |
| `__pow__`(self, other)      | **                |

Example: Overriding `__add__()`
- If we have a **class Purchace** and we want to **sum** all expenses using the `+` operator, we can override the 
`__add__` method
```python
class Purchase:
    def __init__(self, product_name: str, cost: int) -> None:
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other: Purchase):   # `ohter` is object instantiated from the same class
        name = f'{self.product_name}, {other.prduct_name}'
        cost = self.cost + other.cost
        return Purchase(name, cost)

first_product = Purchase('sofa', 650)
second_product = Purchase('table', 150)
print(first_product + second_product)   # sofa, table; 800
```
### "Rich Comparison" Magic Methods
| Magic Methods         | Get Classed Using |
|-----------------------|-------------------|
| `__lt__`(self, other) | <                 |
| `__le__`(self, other) | <=                |
| `__eq__`(self, other) | ==                |
| `__ne__`(self, other) | !=                |
| `__gt__`(self, other) | \>                |
| `__ge__`(self, other) | >=                |

Example: Overriding: `__gt__`()
-If we have a **class Person** and we want to **compare** them by their salary using `>` operator, we can override the
`__gt__` method
```python
class Person:
    def __init__(self, name: str, salary: int) ->None:
        self.name = name
        self.salary = salary

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

person_one = Person('John', 20)
person_two = Person('Natasha', 30)
print(person_one > person_two)      # False
```

## Duck Typing
- Duck Typing is a **type system** used in dynamic languages
- "if it `looks like a duck and walk like a duck and quacks like a duck, it's duck`"
  - i.e., we don't care about **object's type**, but whether **they have a methods** we need
- We **can create a method** `sound()` and call it **no matter** what type the object that makes the sound is
```python
class Cat:
  
    @staticmethod
    def sound(self) -> None:
        print("Meow!")

class Train:
  
    @staticmethod
    def sound(self) -> None:
        print("Sound from wheels slipping!")

for any_type in Cat(), Train():
    any_type.sound()
```

## What is Abstraction
### A Word about Abstraction
- In object-oriented programming, abstraction is one of the **four central principles**
- Through abstraction, we hide all but the relevant data about an object to **reduce complexity** and **increase efficiency**
- Abstraction can be achieved by:
  - Functions and methods
  - `Abstract classes`

### Abstract Classes
- Abstract classes are class that contain one or more **abstract methods** 
  - An abstract method is a method that is **declared** but contains **no implementation**
- Abstract classes my not be instantiated and require **subclasses** to provide implementations for the abstract methods
- It could be achieved using **exceptions**, but it is **not a good practice**
```python
class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise Exception('This is en abstract class')

    def area(self):
        raise Exception('This is an abstract class')

    def perimeter(self):
        raise Exception('This i an abstract class')
```
### Abstract Class with `ABC` Module
- Abstract base classes(ABSs) **enforce** derived classes to implement particular methods from the base class
  - We implement it using the `abc` module
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    
    
    @abstractmethod
    def perimeter(self):
        pass
```
Example: Abstract classes

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def __init__(self, name: str) -> None:
        super.__init__(name)
    
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name: str) -> None:
        super.__init__(name)

    def sound(self):
        print("Meow!")

cat = Cat("Willy")
cat.sound()                 # Meow!
dog = Dog("Willy")
dog.sound()                 # Bark!
animal = Animal("Willy")        
animal.sound()              # Error
```
### Summary
- `Polymorphism` means the same function name is used for different types
- Through `abstraction`, we hide all but the relevant data about an object
- Abstract classes may `not be instantiated`, and require subclasses

### Abbrivations
- The abbreviation “`i.e.`” stands for id est, which is Latin for “`that is`”. 
- The abbreviation “`e.g.`” stands for the Latin phrase exempli gratia, meaning “`for example`”.