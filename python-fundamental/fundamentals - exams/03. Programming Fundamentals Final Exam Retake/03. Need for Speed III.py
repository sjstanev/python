number_of_cars = int(input())
cars = []
for num in range(number_of_cars):
    car, mileage, fuel = input().split('|')
    mileage = int(mileage)
    fuel = int(fuel)
    cars.append({'car': car, 'mileage': mileage, 'fuel': fuel})

max_liter_tank = 75
command = input()
while not command == "Stop":
    command = command.split(' : ')
    car = command[1]

    if command[0] == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        for model in cars:
            if model['car'] == car:

                if model['fuel'] - fuel <= 0:
                    print("Not enough fuel to make that ride")
                else:
                    model['fuel'] -= fuel
                    model['mileage'] += distance
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                    if model['mileage'] > 100_000:
                        print(f"Time to sell the {car}!")
                        cars.remove(model)

    if command[0] == "Refuel":
        fuel = int(command[2])
        for model in cars:
            if model['car'] == car:
                if model['fuel'] + fuel <= max_liter_tank:
                    print(f"{car} refueled with {fuel} liters")
                    model['fuel'] += fuel
                else:
                    print(f"{car} refueled with {max_liter_tank - model['fuel']} liters")
                    model['fuel'] = max_liter_tank

    if command[0] == "Revert":
        kilometers = int(command[2])
        for model in cars:
            if model['car'] == car:
                model['mileage'] -= kilometers
                if model['mileage'] < 10_000:
                    model['mileage'] = 10_000
                else:
                    print(f"{car} mileage decreased by {kilometers} kilometers")
                break


    command = input()

for car in cars:
    print(f"{car['car']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")
