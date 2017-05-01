# Player Intialization

class Player(object):
    # TOTAL = 0
    def __init__(self, name):
        self.name = name
        self.good_points = 0
        self.bad_points = 0

    def __str__(self):
        # TO DO: Fix the formatting
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

    # def add_the_points(self):
        # Player.TOTAL += self.good_points
        # Player.TOTAL += self.bad_points
        # Returns the TOTAL amount of points to trigger the story line
        # return Player.TOTAL


# The code below will be moved into our main file when we are ready
# I suggest asking the user for their name before the story rolls
player_name = str(input("Hi. What would you like your name to be?: "))
new_player = Player(player_name)

# To call the name, use (don't forget to add the module in the front):
print(new_player.name)

# This makes sure the name prints currently into the class
print(new_player)
