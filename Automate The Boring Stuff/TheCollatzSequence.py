def collatz(number):

    if number % 2 == 0:
        print('number // 2')
        return number // 2
    else:
        print('3 * number + 1')
        return 3 * number + 1

while True:
    print('Input your number')
    user_number = input()
    try:
        user_number = int(user_number)

        collatz_number = collatz(user_number)
        print(collatz_number)

        if collatz_number == 1:
            break
    except ValueError:
        print('must enter an integer')