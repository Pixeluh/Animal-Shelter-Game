def run_the_map():

    from msvcrt import getch
    from os import system
    import os
    import random
    import title_screen
    import obstacles
    import player

    # TO DO LIST
    # 1) We need to add limitations to where the player can go. (The player can't go outside of the boundaries.. The game crashes if they do.)
    # 2) Under the check_the_spot(), add the cage code that will interact with the player when they hit a '#'

    the_map = [["---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",  "   ", "----------- Legacy -------------"],
               ["|  ", "   ", "   ", "   ", "   ", "   ", " # ", " # ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "  |",  "   ", "|                              |"],
               ["|  ", " # ", " ! ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "  |",  "   ", "| '!'      -          Obstacle |"],
               ["|  ", " # ", "   ", "   ", "   ", "   ", "   ", " ! ", "   ", "   ", "   ", " # ", " # ", " # ", "   ", "   ", "   ", "  |",  "   ", "| '#'      -       Animal Cage |"],
               ["|  ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " ! ", "   ", " ! ", "   ", "  |",  "   ", "|                              |"],
               ["|  ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", "  |",  "   ", "| Use 'W' 'A' 'S' 'D' to move. |"],
               ["|  ", " ! ", "   ", " ! ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", "  |",  "   ", "|______________________________|"],
               ["|  ", " # ", "   ", "   ", "   ", " ! ", " # ", "   ", " ! ", " # ", "   ", "   ", " ! ", "   ", "   ", "   ", " # ", "  |"],
               ["|  ", " # ", "   ", "   ", "   ", "   ", " # ", "   ", "   ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", "  |"],
               ["|  ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", " # ", "   ", "   ", "   ", "   ", "   ", "   ", " ! ", "  |"],
               ["|  ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "  |"],
               ["|  ", "   ", "   ", " ! ", "   ", "   ", " # ", " # ", " # ", "   ", " ! ", "   ", " # ", " # ", " # ", " # ", "   ", "  |"],
               ["---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---"]]

    def print_the_map(the_map):

        for each_row in the_map:
            print()
            for each_character in each_row:
                print(each_character, end="")

    row = 1
    character = 1
    the_map[row][character] = " X "
    print_the_map(the_map)

    obstacle_list = []

    new_obstacle1 = obstacles.Obstacle("A cat meows at you.", "good")
    new_obstacle2 = obstacles.Obstacle("You found some coins on the ground!", "good")
    new_obstacle3 = obstacles.Obstacle("A snake slithers around you... looking for prey.", "bad")
    new_obstacle4 = obstacles.Obstacle("You stepped in dog poo! Your shoes are now dirty.", "bad")
    new_obstacle5 = obstacles.Obstacle("A random chocolate bar was left here. It looks delicious!", "good")
    new_obstacle6 = obstacles.Obstacle("Player:\t 'What is this random drink??? It's black!.....\nI think it's making me feel sick.'", "bad")
    new_obstacle7 = obstacles.Obstacle("A butterfly just flew past you.", "good")
    new_obstacle8 = obstacles.Obstacle("You looked inside this barrel and found a lot of trash.", "bad")
    new_obstacle9 = obstacles.Obstacle("Player:\t 'Is this a baseball card?\nGuess it is mine now.'", "good")
    new_obstacle10 = obstacles.Obstacle("Player:\t 'It STINKS over here. Ugh...'", "bad")
    new_obstacle11 = obstacles.Obstacle("The trash bin is located here. \nPlayer:\t 'Looks like the trash is full, gross.'", "bad")
    new_obstacle12 = obstacles.Obstacle("You found a stray liter of newborn lizards!\nPlayer:\t 'I think I will just grab one of these lizards...for myself.'", "good")

    obstacle_list.append(new_obstacle1)
    obstacle_list.append(new_obstacle2)
    obstacle_list.append(new_obstacle3)
    obstacle_list.append(new_obstacle4)
    obstacle_list.append(new_obstacle5)
    obstacle_list.append(new_obstacle6)
    obstacle_list.append(new_obstacle7)
    obstacle_list.append(new_obstacle8)
    obstacle_list.append(new_obstacle10)
    obstacle_list.append(new_obstacle11)
    obstacle_list.append(new_obstacle12)

    print()

    def check_the_spot(player_location):

        print("\nPlayer Good Points: \t", player.new_player.good_points)
        print("\n")
        print("Player Bad Points: \t", player.new_player.bad_points, "\n")

        if player_location == " # ":
            # insert the animal/cage code here
            print("HELLO!!!")

        elif player_location == " ! ":
            obstacle_to_use = random.choice(obstacle_list)

            print()
            print(obstacle_to_use)

            if obstacle_to_use.stat == "good":
                obstacle_to_use.obstacle_add_good_points()
            else:
                obstacle_to_use.obstacle_add_bad_points()

        elif player_location > the_map[11][character]:
            print_border_msg()

        elif player_location == the_map[0][character]:
            print_border_msg()

        elif player_location > the_map[row][17]:
            print_border_msg()

        elif player_location == the_map[row][0]:
            print_border_msg()

    def print_border_msg():
        print("HALT. DO NOT GO BEYOND THIS POINT.")
        print("EXECUTION IS LIKELY.")

    def move_up():

        player_location = the_map[row-1][character]
        the_map[row-1][character] = " X "
        the_map[1][1] = "   "
        os.system('cls')
        print_the_map(the_map)
        check_the_spot(player_location)

        return previous_char

    def move_down():

        player_location = the_map[row+1][character]
        the_map[row+1][character] = " X "
        the_map[1][1] = "   "
        os.system('cls')
        print_the_map(the_map)
        check_the_spot(player_location)

        return previous_char

    def move_left():

        player_location = the_map[row][character-1]
        the_map[row][character-1] = " X "
        the_map[1][1] = "   "
        os.system('cls')
        print_the_map(the_map)
        check_the_spot(player_location)

        return previous_char

    def move_right():

        player_location = the_map[row][character+1]
        the_map[row][character+1] = " X "
        the_map[1][1] = "   "
        os.system('cls')
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
