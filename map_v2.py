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

the_map[0][0] = "_X_"
row = 0
character = 0
player_location = the_map[row][character]

print_the_map(the_map)

print()

def move_up():
    """ HIHIII """
    player_location = the_map[row-1][character]
    print(player_location)
    print_the_map(the_map)
def move_down():
    player_location = the_map[row+1][character]
    print(player_location)
    print_the_map(the_map)
def move_left():
    """ HIHIII """
    player_location = the_map[row][character-1]
    print(player_location)
    print_the_map(the_map)
def move_right():
    """ HIHIII """
    player_location = the_map[row][character-1]
    print(player_location)
    print_the_map(the_map)

while(True):
    key = ord(getch())
    if key == 119:
        move_up()
    elif key == 97:
        move_left()
    elif key == 115:
        move_down()
    elif key == 100:
        move_right()

