# Class ans Static Methods

- [Static Methods](#static-methods)
- [Class Methods](#class-methods)
- [Overriding Using Class Methods](#overriding-using-class-methods)
## Static Methods
###  `@staticmehod`
- It **knows nothing** about the **class** or **instance** it is called on
- It **cannot modify** object state or class state
- It should be put outside the class, but it is inside the class where it is **applicable**
- To turn the method into the static, we add a line with `@staticmethod` in front  of the method header
- To call a static method, we could use both the **instance** or the **class**
```python
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

print(Person.is_adult(5))       # False
girl = Person("Amy")
print(girl.is_adult(20))        # True
```
### Benefits
- Shows that a particular method is **independent** of everything else around it
- Often helps to **avoid accident modification** that goes around the original design
- Communicates and enforces **developer intent** about the **class design**
- It is much **easier to test** since it is completely independent from the rest ot the class

## Class Methods
### `@classmethod`
- It is **bound to the class** and not the object of the class
- It can **modify a class state** that would apply across all instances of the class
- To turn a method into a class method, we add a line with `@classmethod` in front of the method header
- We generally use class method to **create factory methods**
```python
class Pizza:
    def __init__(self, ingredients: list[str]) -> None:
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls) -> 'Pizza':
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls) -> 'Pizza':
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiana"])

first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()
```
### Benefits
- Simply provide a **shortcut** for creating new instance object
- Ensures **correct instance creation** of the derived class
- You could **easily follow** the Don't Repeat Yourself (DRY) principle using class methods

## Overriding Using Class Methods

<table>
    <tr style="text-align:center">
        <th style="text-align:center">
            class Person
        </th>
        <th style="text-align:left">
            class Employee(Person)
        </th>
    </tr>
    <tr>
        <td>
        
```
        class Person
            min_age = 0
            max_age =150
        
            def __init__(self, name: str, age: int) -> None:
                self.name = name
                self.age = age
        
            @staticmethod
            def __validagte_age(value: int) -> None:
                if value < Person.min_age or \
                    value > Person.max_age:
                    raise ValueError
            @property
            def age(self):
                return self.__age
            
            @age.setter
            def age(self, value):
                self.__validagte_age(value)
                self.__age = value
```
</td>
<td>
        
```
            class Employee(Person)
                min_age = 16
                max_age =150
            
                def __init__(self, name: str, age: int) -> None:
                    self.name = name
                    self.age = age
                
                # Override all the methods below
                @staticmethod
                def __validagte_age(value: int) -> None:
                    if value < Employee.min_age or \
                        value > Employee.max_age:
                        raise ValueError
                @property
                def age(self):
                    return self.__age
                
                @age.setter
                def age(self, value):
                    self.__validagte_age(value)
                    self.__age = value
```
</td>
    </tr>
</table>

- if the methods **do not rely in state** and they **are the same**, they could be optimized using `@classmethod`
```python
class Person:
    min_age = 0
    max_age = 150
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    @classmethod
    def __validate_age(cls, value):
        if value < cls.min_age or value > cls.max_age:
            # __validate_age() takes the class attributes of class Person
            raise ValueError(f'{value} must be between'
                             f'{cls.min_age} and {cls.max_age}')
    
    @property
    def age(self):
        return self.__age 
    
    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value
        
    
class Employee(Person):
    min_age = 16
    
    # __validate_age() takes the class attribute min_age of class Employee
    def __init__(self, name: str, age: int, salary: int) -> None:
        super().__init__(name, age) # when checking the age of the Employee
        self.salary = salary

```
### Summary
- A **static method** is a method that **knows nothing** about the **class** or **instance** it is called on
- A **class method**, on the other hand, is **bound to the class** and not the object of the class