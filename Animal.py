class Animal(object):
    name = ""
    description = ""
    good = ""
    bad = ""

    def __init__(self, name, description, good, bad):
        self.name = name
        self.description = description
        self.good = good
        self.bad = bad

    def __str__(self):
        output = ""
        output += ("Name: " + self.name
                   + "\nDescription: " + self.description
                   + "\nGood Action: " + self.good
                   + "\nBad Action: " + self.bad)
        return output

    def getDescription(self):
        return self.description

    def getName(self):
        return self.name

    def getGood(self):
        return self.good

    def getBad(self):
        return self.bad

    
