"""
There is a robotics factory. The current project is assembly-line robots.
Each robot has a processing time – it is the time in seconds the robot needs to process a product.
 When a robot is free, it should take a product for processing and log its name, product, and processing start time.
Each robot processes a product coming from the assembly line. A product is coming from the line each second
(so the first product should appear at [start time + 1 second]).
If a product passes the line and there is not a free robot to take it, it should be queued at the end of the line again.
The robots are standing in the line in the order of their appearance.
Input
•	On the first line, you will receive the robots' names and their processing times in the format
    "robotName-processTime;robotName-processTime;robotName-processTime..."
•	On the second line, you will get the starting time in the format "hh:mm:ss"
•	Next, until the "End" command, you will get a product on each line.
Output
•	Every time a robot takes a product, you should print: "{robotName} - {product} [hh:mm:ss]"

Examples
Input:
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End

Output:
ROB - detail [08:00:01]
SS2 - glass [08:00:02]
NX8000 - wood [08:00:03]
NX8000 - apple [08:00:06]
"""
from collections import deque


def robots_def(parm):
    robots_dic = {}
    available_robots = deque()

    for x in parm:
        rob, time = x.split('-')
        robots_dic[rob] = int(time)
        available_robots.append(rob)
    return robots_dic, available_robots


def read_products_def():
    result = deque()
    while True:
        line = input()
        if line == 'End':
            break

        result.append(line)
    return result


def time_in_seconds_def(time_str):
    time_conv = time_str.split(':')
    hour = int(time_conv[0]) * 3600
    minutes = int(time_conv[1]) * 60
    sec = int(time_conv[2])

    time_in_sec = hour + minutes + sec
    return time_in_sec


def time_to_string_def(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)


robots_input = input().split(';')
robots_dictionary, robots_dequeue = robots_def(robots_input)

time_str = input()
time_in_seconds = time_in_seconds_def(time_str)

# Create list with time_processing
time_processing = {}
for k, v in robots_dictionary.items():
    time_processing[k] = v

products = read_products_def()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    product = products.popleft()

    if robots_dequeue:
        current_robot = robots_dequeue.popleft()
        print(f'{current_robot} - {product} [{time_to_string_def(time_in_seconds)}]')
        robots_dictionary[current_robot] -= 1
        if robots_dictionary[current_robot] <= 0:
            robots_dequeue.append(current_robot)
            robots_dictionary[current_robot] = time_processing[current_robot]

    else:
        products.append(product)
        for current_robot in robots_dictionary.keys():
            robots_dictionary[current_robot] -= 1

            if robots_dictionary[current_robot] <= 0:
                robots_dequeue.append(current_robot)
                robots_dictionary[current_robot] = time_processing[current_robot]
