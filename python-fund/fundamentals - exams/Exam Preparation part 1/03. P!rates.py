def add_city(cities: list, city: str, population: str, gold: int):
    # Append city to the list of cities.
    # If you receive a city that has already been received, you have\
    # to increase the population and gold with the given values.

    # rotated through all cities and check\
    # if city is already in the list, just increase 'population' and 'gold'
    in_cities = False
    for x in cities:
        if city == x['city']:
            in_cities = True
            x['population'] += population
            x['gold'] += gold
    if not in_cities:
        # add this city to the list of all cities if the one is not there
        cities.append({'city': city, 'population': population, 'gold': gold})


# Until the "Sail" command is given, you will be receiving cities\
# with their population and gold separated by ||
command = input()
# Create empty list of all cities
cities = []
while not command == "Sail":
    # separate the command to the following arguments: city, population, gold
    city, population, gold = command.split('||')
    # add this city to the list of all cities
    add_city(cities, city, int(population), int(gold))
    # repeat until received command == "Sail"
    command = input()

instruction = input()

while not instruction == "End":
    # separate the command to the following arguments:\
    # "Plunder=>{town}=>{people}=>{gold}"\
    # "Prosper=>{town}=>{gold}"
    instruction = instruction.split('=>')
    town = instruction[1]

    if instruction[0] == "Plunder":
        people = int(instruction[2])
        gold = int(instruction[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        for city in cities:
            if town == city['city']:
                city['population'] -= people
                city['gold'] -= gold
                # If any of those two values (population or gold) reaches zero, the town is disbanded
                if city['population'] <= 0 or city['gold'] <= 0:
                    print(f"{town} has been wiped off the map!")
                    cities.remove(city)

    if instruction[0] == "Prosper":
        gold = int(instruction[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            for city in cities:
                if town == city['city']:
                    city['gold'] += gold
                    print(f"{gold} gold added to the city treasury. {town} now has {city['gold']} gold.")
    # repeat until received command == "End"
    instruction = input()


# if there are any existing settlements on your list of targets, you need to print all of them, in the following format:
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f"{city['city']} -> Population: {city['population']} citizens, Gold: {city['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
