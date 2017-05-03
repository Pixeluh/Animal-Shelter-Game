import player
import map_v2

class Obstacle(object):

    def __init__(self, story, stat):

        self.story = story
        self.stat = stat

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
