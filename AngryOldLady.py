from FileReader import FileReader
class AngryOldLady(FileReader):

    #reads the quiz information from a file and adds it to the object
    def __init__(self, fileName):
        super().__init__(fileName)
        try:
            self.quizFile = open(file_name, "r")
        except IOError as e:
            print("Unable to open the file AngryQuiz.txt. Ending program.\n", e)
            input("\n\nPress the enter key to exit.")
            sys.exit()
        self.beginDialog = next_line(quizFile)
        self.endDialog = next_line(quizFile)
        self.gEnding = next_line(quizFile)
        self.bEnding = next_line(quizFile)
        self.goodPoints = int(0)
        self.badPoints = int(0)
        self.totalPoints = int(0)
        intro, question, answers, correct, incorrect = next_block(file_name) 

    def getGoodPoints(self):
        return self.goodPoints

    def getBadPoints(self):
        return self.badPoints

    def getTotalPoints(self):
        return self.totalPoints
    
    #toString method
    def __str__(self):
        output = ""
        output += ("Good points: " + goodPoints + "\nBad Points: " + badPoints
                    + "\nTotal Points: " + totalPoints)
        return output

    #returns the good ending
    def gEnding(self):
        return self.gEnding


    #returns the bad ending
    def bEnding(self):
        return self.bEnding

    #adds good points for correct answers
    def addGood(self):
        self.goodPoints += 1
        self.totalPoints += 1

    #adds bad points for incorrect answers
    def addBad(self):
        self.badPoints += 1
        self.totalPoints += 1

    #adds total points for neutral answers
    def addTotal(self):
        self.totalPoints += 1

    
