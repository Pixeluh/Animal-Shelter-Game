import title_screen
import map_v2
class Player(object):
    def __init__(self, name):

        self.name = name
        self.good_points = 0
        self.bad_points = 0

    def __str__(self):

        print_player = ""
        print_player += "Player Name:\t" + self.name + "\n"
        print_player += "Good Points:\t" + str(self.good_points) + "\n"
        print_player += "Bad Points:\t" + str(self.bad_points) + "\n"

        return print_player

    def add_good_points(self):

        self.good_points += 5

        return self.good_points

    def add_bad_points(self):

        self.bad_points += 5

        return self.bad_points

player_name = str(input("""
`````````````````````````````````````````````````

What would you like your name to be?:

``````````````````````````````````````````````````\n"""))
new_player = Player(player_name)
