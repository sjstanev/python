
# Encapsulation
Benefits of Encapsulation

- [Encapsulation Definition](#encapsulation-definition)
- [Name Mangling a Variable](#name-mangling-a-variable)
- [Name Mangling a Method](#name-mangling-a-method)
- [Built-in Functions for Accessing Attributes](#built-in-functions-for-accessing-attributes)

## Encapsulation Definition
### What is Encapsulation?
- Packing of data and functions into a single content
- Allows us to put **restrictions** and can **prevent the accidental modification** of data
- To do that, an object's variable can only be changed by an object's method
- Everything written within the Python class (methods and variables) is **public by default**
- However, **Python** implements a week encapsulation 
  - it is **performed by convention rather than being enforced by the language

### Access Modifiers
- How to control access?
  - Using a **single underscore** (protected)
  - Using **double underscore** (making it "private")
  - Using **getter and setter methods** to access private variable
- It is **a matter of convention** to differentiate them into three terms - **public, protected** and **private**

### Single Underscore
- Using a single leading underscore is just a **convention**
- A name prefixed with an single underscore should be treated as a **non-public** methods/ variable

```python
class Person:
    def __init__(self, name: str, age: int=0) -> None:
        self.name = name
        self._age = age

person = Person('Peter', 25)
print(person.name)  # Peter
print(person._age)  # 25
```
### Double Underscore
- When naming an attribute with **two leading underscore**, it invoke **name mangling**
- In Python, mangling is used for attributes that one class **does not want subclass to use**
- Python **does not restrict access** to such attributes
- It is still possible to **access** or **modify** a variable that is considered "private" **from outside** the class
```python
class Person:
    def __init__(self, name: str, age:int=0) -> None:
        self.name = name
        self.__age = age

    def info(self):
        print(f"I am {self.name}, {self.__age} years old.")

person = Person('Peter', 25)

# accessing data using the class method
person.info()           # I am Peter, 25 years old.

# accessing data directly from outside
print(person.name)      # Peter
print(person.__age)     # AttributeError: 'Person' object has no attribute '__age'
```
## Name Mangling a Variable
- Used to show that the variable **should not be accessed** from outside the class
```python
class Car:
    def __init__(self) -> None:
        self.__max_speed: str =200

    def drive(self) -> str:
        print('driving max speed ' + str(self.__max_speed))
        
red_car = Car()
red_car.drive()                 # driving max speed 200    
red_car.__max_speed = 10        # won't change because it is name mangled
red_car.drive()                 # driving max speed 200
```
### Getter and Setter Methods
- Used to **access and change** the `private` variables as they are part of the class
```python
class Person:
    def __init__(self, name: str, age:int=0) -> None:
        self.name = name
        self.__age = age

    def info(self) -> str:
        print(self.name)
        print(self.__age)

    def get_age(self) -> str:          # getter
        print(self.__age)   

    def set_age(self) -> None:          # setter    
        self.__age = age

person = Person('Peter', 25)

# accessing data using class method
person.info()           # Peter
                        # 25

# changing age using setter
person.set_age(36)
person.get_age()        # 36
```
### Getters and Setters
- The `pythonic` way of defining **getters and setters** is using **properties**
- By defining properties, you can **change** the **internal implementation** of a class without affecting the program
```python
class Person:
    def __int__(self, age: int=0) -> None:
        self.age = age

    @property
    def age(self) -> str:
        return self.__age = age

    @age.setter
    def age(self, age):
        if age < 18: self.__age = 18
        else: self.__age = age

person = Person(25)
print(person.age)       # 25
person.age = 10
print(person.age)       # 18
```
- You should use Python properties to **apply rules** to attribute
```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, value: int) -> Union[str, int]:
        if value <= 0:      # An exception will be thrown on any attempt to violate the rule
            raise Exception("Age must be greater than zero")
        self.__age = value
```
## Name Mangling a Method
- It is **class method** that should only be called from **inside the class** where it is defined
```python
class Person:
    def __init__(self) -> None:
        self.first_name = 'Peter'
        self.last_name = 'Parker'

    def __full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def info(self) -> str:
        return self.__full_name()

person = Person()
print(person.info())                # Peter Parker
print(person.__full_name())         # AttributeError
print(person._Peter__full_name())   # Peter Parker
```
## Built-in Functions for Accessing Attributes
### Get Attribute Function
- **getter()** - used to access the attribute of an object
- Returns **the value** of the named attribute
- The method takes multiple parameters
  - `Object`
  - `Name`
  - `Default (optional)`
```python
class Person
    def __init(self, name: str) -> None:
        self.name = name

person = Person('Peter')
print(getattr(person, 'name'))              # True
print(getattr(person, 'age'))              # AttributeError
print(getattr(person, 'age', 'None'))       # None
```

### __getattr__()
- Called when attribute lookup **has not found** the attribute in the usual places
- The method takes **one** parameters - **the name of the attribute**
```python
class Phone:
    def __getattr__(self, attr: str) -> None:
        return None

phone = Phone()
print(phone.color)                  # None
print(getattr(phone, 'size'))       # None
```
- When accessing **phone.color**, Python class `phone.__getattr__('color')`

### Has Attribute Function
- `hasattr()` - checks if an attribute exists or not
- Returns `True` if an object has the given named attribute and `False` if it does not
- The method takes two parameters:
  - `Object`
  - `Name`
```python
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

person = Person('Peter')
print(hasattr(person, 'name'))  # True
print(hasattr(person, 'age'))   # False
```
### Set Attribute Function
- `setattr()` - used to set the value of the attribute
- Returns `None`
- The method takes three parameters:
  - `Object`
  - `Name`
  - `Value`
```python
class Person:
    def __init__ (self, name: str) -> None:
        self.name = name

person = Person('Peter')
print(setattr(person, 'name', 'George'))    # None
print(person.name)                          # George   
print(setattr(person, 'age', '21'))         # None
print(person.age)                           # 21
```
### __setattr__()
- Called when an attribute **assignment is attempted**
- The method takes two parameters:
  - The `name` of attribute
  - The `value`we want to assign to the attribute
```python
class Phone:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value.upper()

phone = Phone()
phone.color = 'black'
print(phone.color)      # BLACK
``` 
### Delete Attribute Function
- `delattr()` - deletes an attribute from the object
- if you are accessing the attribute after deleting it raise **AttributeError**
- The methods takes two parameters:
  - `Object`
  - `Name`
```python
class Person:
    def __init__(self, name):
        self.name = name
        
person = Person('Peter')
print(person.name)              # 'Peter'
print(delattr(person, 'name'))  # None
print(person.name)              # AttributeError
```
### __delattr__()
- Called when an attribute **deletion is attempted**
- The methods takes one parameter
  - The `name` of the attribute
- It should only be implemented if `del obj.name` is `meaningful` for the object
```python
class Phone:
    def __delattr__(self, attr):
        del self.__dict__[attr]
        print(f"'{str(attr)}' was deleted")
        
phone = Phone()
phone.color = 'black'
del phone.color         # 'color' was deleted
```
### Summary
- `Encapsulation` is packing of data and functions into single component
- `Name mangling` is used for attributes that one class does now want subclass to use
- The `property decorator` is the pythonic way of using getters and setters
- We could use built-in functions for **accessing attributes**