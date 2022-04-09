def rate(plants_list: list, plant: str, rating: int):
    for x in plants:
        if x['plant'] == plant:
            x['rating'] = rating
            print(x)

number_of_plant = int(input())

# Create empty list that will contain all information about the plants
plants = []

for i in range(number_of_plant):
    plant_value, rarity_value = input().split('<->')
    plants.append({'plant': plant_value, 'rarity': rarity_value})
print(plants)
command = input()

# Until you receive the command "Exhibition", you will be given some of these commands:
while not command == 'Exhibition':
    # command looks like: "Rate: {plant} - {rating}"
    command = command.split(':')
    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        rate(plants, plant, int(rating))


    if command[0] == 'Update':
        pass
    if command[0] == 'Reset':
        pass


    command = input()


