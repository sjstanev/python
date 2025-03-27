def rhombus_of_stars(number_of_stars):
    """
    Reads a positive integer and returns the number of rhombus of stars.
    :return: returns the number of rhombus of stars.
    """

    draw_upper_part(number_of_stars)
    draw_bottom_part(number_of_stars)


def draw_upper_part(n):
    """
    Will draw a upper part of rhombus of stars.
    :param n: number of rhombus of stars.
    :return: upper part of rhombus of stars.
    """

    for i in range(1, n + 1):
        draw_row(n, i)

def draw_bottom_part(n):
    """
    Will draw a bottom part of rhombus of stars.
    :param n: number of rhombus of stars.
    :return: bottom part of rhombus of stars.
    """
    for i in range(n , 0, -1):
        draw_row(n, i)


def draw_row(number_of_stars, i):
    """
    This will draw a row of rhombus of stars.
    :param number_of_stars: *
    :param i: looping through the number of stars.
    :return: print(f"{' ' * (n - i)}{'* ' * i}")
    """

    print(f"{' ' * (number_of_stars - i)}{'* ' * i}")

rhombus_of_stars(3)