# Advent of Code
import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def fuel_calculator(mass):
    while True:
        new_fuel = (round_down(int(mass) / 3)) - 2
        if new_fuel > 0:
            return new_fuel + fuel_calculator(new_fuel)
        else:
            return 0


def fuel_requirement(file='day1_input.txt'):
    fuel = 0
    with open(file, "r") as f:
        for lines in f:
            fuel += fuel_calculator(lines)
        print(fuel)



fuel_requirement()
