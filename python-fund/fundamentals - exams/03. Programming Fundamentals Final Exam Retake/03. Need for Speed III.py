number_of_cars = int(input())
cars = []
for num in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    cars.append({'car': car, 'mileage': mileage, 'fuel': fuel})

command = input()
while not command == "Stop":
    command = command.split(' : ')

    if command[0] == "Drive":
        pass
    if command[0] == "Refuel":
        pass
    if command[0] == "Revert":
        pass
    command = input()
