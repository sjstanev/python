class Stack:
    def __init__(self):
        self.data: list[str] = []

    def push(self, element: str) -> None:
        if not isinstance(element, str):
            raise TypeError("Expected a string")
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return self.data == []

    def __str__(self) -> str:
        result = ', '.join(map(str, reversed(self.data)))
        return result


s = Stack()
print(s.is_empty())
print(s.data)
print(s.push("a"))
print(s.push("b"))
print(s.push("c"))
print(s.is_empty())
print(s.data)
print(s.top())
print(s.pop())
print(s.data)
print(s.top())