def rate(plants_list: list, plant: str, rating: int):
    is_valid = False
    #add the given rating to the plant (store all ratings) - {average_rating}
    for x in plants_list:
        if x['plant'] == plant:
            # if key exist add average_rating
            if 'rating' in x.keys():
                x['rating'] = (x['rating'] + rating)/2
            # otherwise, create new one and average_rating
            else:
                x['rating'] = rating
            is_valid = True
    if not is_valid:
        print('error')

def update(plants_list: list, plant: str, rarity: int):
    is_valid = False
    #{plant} - {new_rarity} – update the rarity of the plant with the new one
    for x in plants_list:
        if x['plant'] == plant:
            x['rarity'] = rarity
            is_valid = True
    if not is_valid:
        print('error')

def reset(plants_list: list, plant: str):
    is_valid = False
    # remove all the ratings of the given plant
    for x in plants_list:
        if x['plant'] == plant:
            x['rating'] = 0
            is_valid = True
    if not is_valid:
        print('error')


number_of_plant = int(input())

# Create empty list that will contain all information about the plants
plants = []

for i in range(number_of_plant):
    plant_value, rarity_value = input().split('<->')
    plants.append({'plant': plant_value, 'rarity': rarity_value})

command = input()

# Until you receive the command "Exhibition", you will be given some of these commands:
while not command == 'Exhibition':
    # command looks like: "Rate: {plant} - {rating}"
    command = command.split(':')

    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        plant = plant.strip()
        rate(plants, plant, int(rating))

    if command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        plant = plant.strip()
        update(plants, plant, int(new_rarity))

    if command[0] == 'Reset':
        plant = command[1]
        plant = plant.strip()
        reset(plants, plant)


    command = input()
print('Plants for the exhibition:')
for plant in plants:
    print(f"- {plant['plant']}; Rarity: {plant['rarity']}; Rating: {plant['rating']:.2f}")

