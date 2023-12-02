"""
Input:
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

Output:
"{number} - {count} times"

-2.5 - 3 times
4.0 - 2 times
3.0 - 4 times
-5.5 - 1 times
"""
numbers_sting = input()

occurrence_count = {}

numbers = [float(x) for x in numbers_sting.split(' ')]

for number in numbers:
    # Not the best solution
    # occurrence_count[number] += 1
    # if number in occurrence_count:
    #     occurrence_count[number] += 1
    # else:
    #     occurrence_count[number] = 1

    if number not in occurrence_count:
        occurrence_count[number] = 0
    occurrence_count[number] += 1

for number, count in occurrence_count.items():
    print(f"{number:.1f} - {count} times")
