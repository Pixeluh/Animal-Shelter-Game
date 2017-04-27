import player
# Obstacle Intialization
class Obstacle(object):
    def __init__(self, name, story):
        self.name = name
        self.story = story

        # use the text files when making an Obstacle
        # name = "Larry The Snake"
        # story = "larry bit you, ect"
        # stat = Which stat is going to be affected? (good or bad)

    def __str__(self):
        output = ""
        output += "Name: \t" + self.name + "\n"
        output += "Story: \t" + self.story + "\n"
        return output

    def obstacle_add_good_points(self):
        player.new_player.add_good_points()

    def obstacle_add_bad_points(self):
        player.new_player.add_bad_points()


# testing the obstacle creation
# Get text from a file and save them variables
# Then use the variables when creating an instance
new_obstacle = Obstacle("Larry The Snake", "He bit you! Run away!")
new_obstacle1 = Obstacle("Lemon The Cat", "Lemon purrs...")
new_obstacle2 = Obstacle("SnakeMan the Hippo", "Fuck u say to me??")

# When we run into an obstacle, just run the appropriate function to deduct
# points from the player stat
#new_obstacle.obstacle_add_bad_points()
