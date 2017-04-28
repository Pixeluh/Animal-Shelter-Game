import obstacles
import player
import random

map_slots = []
obstacle_list = []

# creating obstacles
new_obstacle1 = obstacles.Obstacle("Lemon The Cat", "Lemon purrs...", "#")
new_obstacle2 = obstacles.Obstacle("SnakeMan the Hippo", "Fuck u say to me??", "#")
new_obstacle3 = obstacles.Obstacle("Bird Poo", "Gross!", "#")
new_obstacle4 = obstacles.Obstacle("Candy", "Yum!", "#")

obstacle_list.extend(new_obstacle1.symbol)
obstacle_list.extend(new_obstacle2.symbol)
obstacle_list.extend(new_obstacle3.symbol)
obstacle_list.extend(new_obstacle4.symbol)

flooring = "_"

map_slots.extend(obstacle_list)
map_slots.extend(flooring)
map_slots.extend(flooring)
map_slots.extend(flooring)
map_slots.extend(flooring)
map_slots.extend(flooring)
map_slots.extend(flooring)

def map_creation():
    the_map = []
    the_current_row = []
    for x in range(60):
        random_num = random.randrange(0, 10)
        if random_num % 20 == 0:
            the_current_row.append("#")
        else:
            the_current_row.append("_")
             # the_current_row.append(random.choice(map_slots))
        random_num = random.randrange(0, 10)
    for i in range(15):
        the_map.append(the_current_row)

    return the_map

def print_the_map(map, top_border, side_border):
    border = " "
    for x in range(0, len(map[0]) * len(map[0][0])):
        border += top_border
    border += " "
    print(border)
    for every_row in map:
        print(side_border, end="")
        for every_character in every_row:
            print(every_character, end="")
        print(side_border, end="")
        print()
    print(border)

game_map = map_creation()
print_the_map(game_map, "-", "|")
