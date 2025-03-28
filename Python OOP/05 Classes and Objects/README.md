# Class and Objects

- [Classes and Instances](#classes-and-instances)
- [Attributes](#attributes)
- [Methods](#methods)
- [Data Attributes](#data-attributes)
- [Special Data Attributes](#special-data-attributes)

## Classes and Instances
### Class Object
Classes support two kinds of operations:
 - **attribute references** - access them using `.` operator
 - **instantiation** - uses **function notations**
```python
class Example:
    text = 'Hello World!'

    def print_text(self):
        return 'Tom and Jery'

Example.text        # attribute reference
Example.print_text  # attribute reference
x = Example()       # instantiation
```
### Instantiation
- It is known as `calling` the class
- Creates an `empty object` - new instance of the class
- Assign the object to a `local variable`
```python
class Person:
    name = "Stan"
    age = 45
         
person = Person()
         
print(person.name) # Stan
print(person.age) # 45
```
## \_\_init\_\_()
- Creates objects with instances, customized to a `specific initail state`
- `Automatically invoked` for the newly created class instance
```python
class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
my_laptop = Laptop("Inspiron 15", "Dell")
```
### `Self` Parameter
- `self` is used to represent the instance of the class
- It `binds` the attributes with the given arguments
- It is `not a keyword` but using it increases the readability of the code
```python
class Laptop:
    def __init__(self, name, model):    # instance's arguments
        self.name = name                # instance's attributes
        self.model = model              # instance's attributes
    
my_laptop = Laptop("Inspiron 15", "Dell")
```
### Instance Objects
- Instances support only one kind of operation
  - `attribute reference - access` them using `.` operator
```python
class Laptop:
    pass

my_laptop = Laptop("Inspiron 15", "Dell")
print(my_laptop.name)       # Inspiron 15
print(my_laptop.mode)       # Dell
```
## Attributes
- `Data` and `procedure` that "belong" to the class
- Valid attribute names are the ones **in the class's namespaces**
- There are two kinds of attribute references:
  - `Methods`
  - `Data attribute`

### Instance Methods
- Define the `behavior` of the object
- The `instance object` is passed as a `first argument` of the method - using `self` by convention
```python
class MyClass:
    def say_hello(self): 
        return 'Hello'

x = MyClass()
x.say_hello()           # conventional way 
MyClass.say_hello(x)    # equivalent
```
### Special / Dunder Methods
- `Built-in methods` that you can define to add "`magic`" to your classes
- Surrounded by **double underscore** e.g.,__init__()
- `Enrich` the class design end enhance the readability
```python
class Dog:
    def __init__(self, name):
        self.name = name

x = Dog("Max")
print(x.__dict__)   # {"name": "Max"}
```
## Methods
- We could **change the state** of the object using methods
```python
class Dog:
    def __init__(self, name):
        self.name = name
        
    def change_name(self, new_name):
        self.name = new_name
        
x = Dog("Max")
x.change_name("Rex")
print(x.name)           # Rex
```
### __str__()
- returns a printable `string representation` of any user-defined class
```python
class MyClass:
    def __str__(self):
        return 'This is My Class'
    
    
my_instance = MyClass() 

print(str(my_instance))         # This is My Class
print(my_instance.__str__())    # This is My Class
print(my_instance)              # This is My Class
```
### __repr__()
- returns a `machine-readable or console representation`  of any user-defined class
```python
class MyClass:
    def __repr__(self):
        return 'This is My Class'
    
    
my_instance = MyClass() 

print(repr(my_instance))         # This is My Class
print(my_instance.__repr__())    # This is My Class
print(my_instance)               # This is My Class
# use print() only when __repr__() return string
```
## Data Attributes
- Values that are `stored internally` and are `unique` to that object
- They define the `state` of the object
- There are two types of data attributes:
  - `Instance variable` - are unique to each instance
  - `Class variable` - are shared by all instances of the class

```python
class Laptop:
    brand = "Dell"                  # class variable

    def __init__(self, name):
        self.name = name            # instance variable

first_laptop = Laptop("Latitude 5300")
second_laptop = Laptop("Inspiron 15")
print(first_laptop.brand == second_laptop.brand)    # True
print(first_laptop.name == second_laptop.name)      # False
```
- It is `not` a good practice to `declare` or `remove` data attributes `outside the class`
- `Instance variables` are independent from one instance to the other
- Modifying a `class variable` affect all object instances at the same time

```python
class Dog:
    tricks = []

    # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
        
poodle = Dog("Bella")
beagle = Dog("Max")

poodle.tricks.append('roll over')
print(beagle.tricks)                # shared by all dogs ['roll over']
```
### Good Practice
```python
class Dog:
    kind = 'canine' # class variable shared by all instances
    
    def __init__(self, name):
        self.name = name
        self.tricks = []
        
# creates empty list for each dog
poodle = Dog("Bella")
beagle = Dog("Max")

print(poodle.name, poodle.kind) # Bella canine
print(beagle.name, beagle.kind) # Max canine

poodle.tricks.append('roll over')
beagle.tricks.append('play dead')

print(poodle.tricks)        # ['roll over']
print(beagle.tricks)        # ['play dead']
```

## Special Data Attributes
### __doc__ Attribute
- Provide `documentation` of the object as a **string**
```python
class MyClass:
    """This is MyClass."""
    
    def example(self):
    """This is the example module of MyClass."""
        pass

print(MyClass.__doc__)              # This is MyClass.
print(MyClass.example.__doc__)      # This is the example method of MyClass.
```
### __dict__ Attribute
- This is a dictionary containing a`module's symbol table`
```python
class MyClass:
    class_variable = 1
    
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
        
first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__)     # {'__module__': '__main__', ... }
print(first.__dict__)       # { 'instance_variable': 2 }
print(second.__dict__)      # { 'instance_variable': 3 }
```
## Summary
- `Instance` object are individual object of a class
- `Methods` are functions that belong to an object
- `Instance variable` are unique to each instance
- `Class Variables `are shared by all instances