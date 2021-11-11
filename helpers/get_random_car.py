from random import choice, random


def get_lines(filename):
    lines = []

    file = open(filename)
    for line in file:
        lines.append(line.strip())

    file.close()

    return lines


def get_random_car():
    cars = get_lines('./helpers/cars.txt')
    random_car = choice(cars)

    return random_car
