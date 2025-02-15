"""
Examples
Input:
ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
"""
from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(';')
    for robot_input in robots_input:
        robot_details = robot_input.split('-')
        name = robot_details[0]
        processing_time = int(robot_details[1])
        result[name] = processing_time
    return result


def read_products():
    results = deque()
    while True:
        line = input()
        if line == 'End':
            break
        results.append(line)

    return results


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
    seconds %= 3600  # second = second % 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)


robots = read_robots()
available_robots = [k for k in robots.keys()]
processing_robots = {}

time_str = input()
time_in_seconds = time_in_seconds_def(time_str)

products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{time_to_string_def(time_in_seconds)}]')
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)

divmod()