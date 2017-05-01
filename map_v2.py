# map (hard coded version)

from msvcrt import getch
from os import system
import os
import random
import obstacles
import player

the_map = [["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "_#_", "___", "___", "___", "___", "_#_", "___", "___"],
           ["___", "_#_", "_!_", "___", "___", "___", "_#_", "___", "___"],
           ["___", "_#_", "___", "___", "___", "___", "_#_", "_!_", "___"],
           ["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "_!_", "___", "_!_", "___", "___", "___", "___", "___"],
           ["___", "_#_", "___", "___", "___", "_!_", "_#_", "___", "___"],
           ["___", "_#_", "___", "___", "___", "___", "_#_", "___", "___"],
           ["___", "_#_", "___", "___", "___", "___", "___", "___", "___"],
           ["_!_", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "___", "___", "_!_", "___", "___", "_#_", "___", "___"],
           ["___", "___", "___", "_#_", "_#_", "_#_", "___", "___", "___"]]

def print_the_map(the_map):
    print("***************************", end="")
    for each_row in the_map:
        print()
        for each_character in each_row:
            print(each_character, end="")
    print("\n***************************")
    print("\n\n")
    print("-- Legacy -- ")
    print("Use WASD to move.")
    print("! = Obstacles")
    print("# = Animal Cages")

row = 0
character = 0
the_map[row][character] = "_X_"

print_the_map(the_map)


obstacle_list = []
new_obstacle1 = obstacles.Obstacle("Lemon The Cat", "Lemon purrs...", "good")
new_obstacle2 = obstacles.Obstacle("SnakeMan the Hippo", "Fuck u say to me??", "bad")
new_obstacle3 = obstacles.Obstacle("Bird Poo", "Gross!", "good")
new_obstacle4 = obstacles.Obstacle("Candy", "Yum!", "bad")

obstacle_list.append(new_obstacle1)
obstacle_list.append(new_obstacle2)
obstacle_list.append(new_obstacle3)
obstacle_list.append(new_obstacle4)

print()

def check_the_spot(player_location):
    if player_location == "_#_":
        # insert animal cage stuff
        print("HELLO!!!")
    elif player_location == "_!_":
        # insert obstacle stuff
        obstacle_to_use = random.choice(obstacle_list)
        print()
        print(obstacle_to_use)
        if obstacle_to_use.stat == "good":
            obstacle_to_use.obstacle_add_good_points()
        else:
            obstacle_to_use.obstacle_add_bad_points()
    print("Player Good Points: \t", player.new_player.good_points)
    print("\n")
    print("Player Bad Points: \t", player.new_player.bad_points)

def move_up():
    """ HIHIII """
    player_location = the_map[row-1][character]
    # print("\n", "Spot: \t", player_location, "\n")
    the_map[row-1][character] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
    check_the_spot(player_location)
    return previous_char
def move_down():
    player_location = the_map[row+1][character]
    # print("\n", "Spot: \t", player_location, "\n")
    the_map[row+1][character] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
    check_the_spot(player_location)
    return previous_char
def move_left():
    """ HIHIII """
    player_location = the_map[row][character-1]
    # print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character-1] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
    check_the_spot(player_location)
    return previous_char
def move_right():
    """ HIHIII """
    player_location = the_map[row][character+1]
    # print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character+1] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
    check_the_spot(player_location)
    return previous_char

while(True):
    key = ord(getch())
    if key == 119:
        previous_char = the_map[row-1][character]
        move_up()
        row -= 1
        the_map[row][character] = str(previous_char)
    elif key == 97:
        previous_char = the_map[row][character-1]
        move_left()
        character -= 1
        the_map[row][character] = str(previous_char)
    elif key == 115:
        previous_char = the_map[row+1][character]
        move_down()
        row += 1
        the_map[row][character] = str(previous_char)
    elif key == 100:
        previous_char = the_map[row][character+1]
        move_right()
        character += 1
        the_map[row][character] = str(previous_char)

# TO DO:
# Set up limitations for movement. (If we move out of the boundry the game crashes)
# Add obstacle/cages to the map
