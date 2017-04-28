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

row = 0
character = 0
the_map[row][character] = "_X_"

print_the_map(the_map)

print()

def move_up():
    """ HIHIII """
    player_location = the_map[row-1][character]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row-1][character] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
def move_down():
    player_location = the_map[row+1][character]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row+1][character] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
    return previous_char
def move_left():
    """ HIHIII """
    player_location = the_map[row][character-1]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character-1] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
    return previous_char
def move_right():
    """ HIHIII """
    player_location = the_map[row][character+1]
    print("\n", "Spot: \t", player_location, "\n")
    the_map[row][character+1] = "_X_"
    the_map[0][0] = "___"
    print_the_map(the_map)
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
# Replace the characters as we move
# Set up limitations for movement. (If we move out of the boundry the game crashes)
# Add a legend below the map
# Add obstacle/cages to the map
