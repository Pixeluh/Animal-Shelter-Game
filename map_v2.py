# map (hard coded version)

from msvcrt import getch
from os import system


the_map = [["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "_H_", "___", "___", "___", "___", "_H_", "___", "___"],
           ["___", "_H_", "_!_", "___", "___", "___", "_H_", "___", "___"],
           ["___", "_H_", "___", "___", "___", "___", "_H_", "_!_", "___"],
           ["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "_!_", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "_H_", "___", "___", "___", "_!_", "_H_", "___", "___"],
           ["___", "_H_", "___", "___", "___", "___", "_H_", "___", "___"],
           ["___", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["_!_", "___", "___", "___", "___", "___", "___", "___", "___"],
           ["___", "___", "___", "_!_", "___", "___", "___", "___", "___"],
           ["___", "___", "___", "_H_", "_H_", "_H_", "___", "___", "___"]]

def print_the_map(the_map):
    for each_row in the_map:
        print()
        for each_character in each_row:
            print(each_character, end="")

#the_map[0][0] = "_X_"
row = 0
character = 0

print_the_map(the_map)

print()

def move_up():
    """ HIHIII """
    player_location = the_map[row-1][character]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character] = "___"
    the_map[row-1][character] = "_X_"
    print_the_map(the_map)
def move_down():
    player_location = the_map[row+1][character]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character] = "___"
    the_map[row+1][character] = "_X_"
    print_the_map(the_map)
def move_left():
    """ HIHIII """
    player_location = the_map[row][character-1]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character] = "___"
    the_map[row][character-1] = "_X_"
    print_the_map(the_map)
def move_right():
    """ HIHIII """
    player_location = the_map[row][character-1]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character] = "___"
    the_map[row][character+1] = "_X_"
    print_the_map(the_map)

while(True):
    key = ord(getch())
    if key == 119:
        move_up()
        row -= 1
    elif key == 97:
        move_left()
        character -= 1
    elif key == 115:
        move_down()
        row += 1
    elif key == 100:
        move_right()
        character += 1

# TO DO:
# Replace the characters as we move
# Set up limitations for movement. (If we move out of the boundry the game crashes)
# Add a legend below the map
# Add obstacle/cages to the map
