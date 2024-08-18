import random


def create_coin_flip_store():
    coin_flip_streaks = []
    for i in range(100):
        flip = random.randint(0, 1)
        coin_flip_streaks.append(flip)
    return coin_flip_streaks


def issix_streaks(param):
    counter = 1
    matches_streaks = [param[0]]

    for i in range(1, len(param)):

        if param[i] == matches_streaks[-1]:
            matches_streaks.append(param[i])
            counter += 1
        else:
            counter = 1
            matches_streaks.clear()
            matches_streaks.append(param[i])

        if counter == 6:
            return matches_streaks


numberOfStreaks = 0
for experiment in range(10000):

    coin_flip = create_coin_flip_store()
    if issix_streaks(coin_flip) is not None:
        numberOfStreaks += 1

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
