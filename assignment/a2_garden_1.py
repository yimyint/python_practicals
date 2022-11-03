"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Zar Chi Oo
Date started: 14 September 2022
Pseudocode:
function main():
    day=0
    food=[0]
    display welcome message
    get user choice
    if user choice is equal to N
        display plants
    else
        plants = l
        display ("Loaded")
    print("You start with these plants:")
    display_plant_list(plants)
    display_menu(food, day, plants)
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "D":
            display_plant_list(plants)
            display_menu(food, day, plants)
            choice = input("Choose: ").upper()





"""

import random

MAXIMUM_RAINFALL = int(128)
MINIMUM_RAINFALL = int(0)
REQUIRED_RAINFALL = int(32)

def main():
    day = 0
    total_food = [0]
    max_rainfall = MAXIMUM_RAINFALL
    min_rainfall = MINIMUM_RAINFALL
    require_rainfall = REQUIRED_RAINFALL

    filename = "plants.txt"
    print("Welcome to my garden.\nPlants cost and generate food according to their name length (e.g., Sage plants "
          "cost 4).\nYou can buy new plants with the food your garden generates.\nYou get up to 128 mm of rain per "
          "day. Not all plants can survive with less than 32.\nEnjoy :)")

    user_choice = input("Would you like to load your plants.txt (Y/n)").upper()
    if user_choice == "N":
        plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
    else:
        plants = load_file(filename)
        print("Loaded")
    print("You start with these plants:")
    display_plant_list(plants)
    display_menu(total_food, day, plants)
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "D":
            display_plant_list(plants)
        elif choice == "W":
            print("Wait")
            simulate_day(plants, total_food, min_rainfall, max_rainfall,require_rainfall)
            day += 1
        elif choice == "A":
            add_plant(plants, total_food)
        else:
            print("Invalid Choice")
        display_menu(total_food, day, plants)
        choice = input("Choose: ").upper()
    else:
        if len(plants) > 0:
            print('You finished with these plants')
            display_plant_list(plants)
        else:
            print("You finished with no plants")
        print(f"\nAfter {day} days, you have {len(plants)} plants and your total food is {total_food[0]}.")
        file_save_choice = input("Would you like to save your plants to plants.txt (Y/n)? ").upper()
        if file_save_choice != "N":
            save_plants_to_file(filename, plants)
            print("Saved.")
            print("Thank you for simulating. Now enjoy some real plants.")

def save_plants_to_file(filename, plants):
    out_file = open(filename, 'w')
    for plant in plants:
        print(plant, file=out_file)
    out_file.close()

def add_plant(plants, total_food):
    new_plant = input("Enter plant name: ").title()
    while new_plant == "":
        print("Invalid plant name")
        new_plant = input("Enter plant name: ").title()
    else:
        while new_plant in plants:
            print(f"You already have a {new_plant} plant.")
            new_plant = input("Enter plant name: ").title()
        else:
            if is_affordable(new_plant, total_food):
                print(f"{new_plant} would cost {len(new_plant)} food. With only {total_food[0]}, you can't afford it")
            else:
                plants.append(new_plant)
                total_food[0] -= len(new_plant)


def is_affordable(plant, total_food):
    if len(plant) > total_food[0]:
        return True
    return False

def remove_plant(plants):
    if len(plants) > 0:
        dead_plant_index = random.randint(0, len(plants) - 1)
        dead_plant = plants[dead_plant_index]
        print(f"Sadly your {dead_plant} plant has died")
        plants.remove(dead_plant)

def simulate_day(plants, total_food, min_rainfall, max_rainfall, require_rainfall):
    total_food_made = 0
    rainfall = int(random.randint(min_rainfall, max_rainfall))
    percent = random.randint(int(1 / 3 * rainfall), rainfall) / 128
    print("rainfall:" + str(rainfall) + "mm")
    if rainfall < require_rainfall:
        remove_plant(plants)
    for i in plants:
        food_made = generate_food(i, percent)
        print(f"{i} produced {food_made}", end=", ")
        total_food_made += food_made
    total_food[0] += total_food_made

def generate_food(plant, percent):
    return int(percent * len(plant))

def display_plant_list(plants):
    for i in plants:
        print(i, end=", ")

def load_file(filename):
    plant_list = []
    in_file = open(filename, 'r')
    for line in in_file:
        plant_list.append(line.strip())
    in_file.close()
    return plant_list

def display_menu(total_food, day, plants):
    print(f"\nAfter {day} days, you have {len(plants)} plants and your total food is {total_food[0]}.")
    print("(W)ait\n(D)isplay plant\n(A)dd new plant\n(Q)uit")

main()
