# show how much the wrong stack is slower than normal one
import time

s = []
count = 2 ** 17
result = 0

start_time = time.time()
for i in range (count):
    s.append(i)

while s:
    result += s.pop()

end_time = time.time()
print(end_time - start_time)

start_time = time.time()
for i in range(count):
    s.insert(0, i)

while s:
    result += s.pop(0)

end_time = time.time()
print(end_time - start_time)