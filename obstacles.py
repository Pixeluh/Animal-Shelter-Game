import player
import map_v2
# Obstacle Intialization
class Obstacle(object):
    def __init__(self, story, stat):
        self.story = story
        self.stat = stat

        # use the text files when making an Obstacle
        # name = "Larry The Snake"
        # story = "larry bit you, ect"
        # stat = Which stat is going to be affected? (good or bad)

    def __str__(self):
        output = ""
        output += "**--**--****--**--****--**--****--**--**\n"
        output += "\n"
        output += self.story + "\n"
        output += "\n"
        output += "**--**--****--**--****--**--****--**--**\n"
        return output

    def obstacle_add_good_points(self):
        player.new_player.add_good_points()

    def obstacle_add_bad_points(self):
        player.new_player.add_bad_points()


# testing the obstacle creation
# Get text from a file and save them variables
# Then use the variables when creating an instance
#new_obstacle = Obstacle("Larry The Snake", "He bit you! Run away!")

# When we run into an obstacle, just run the appropriate function to deduct
# points from the player stat
#new_obstacle.obstacle_add_bad_points()
