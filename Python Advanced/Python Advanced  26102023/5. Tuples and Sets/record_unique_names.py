n = int(input())

names_set = set()

for _ in range(n):
    names_set.add(input())

[print(name) for name in names_set]
