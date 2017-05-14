import sys
import random
class FileReader(object):

    def next_line(self, the_file):
        line = the_file.readline()
        line = line.replace("/", "\n")
        return line

    def next_block(self, the_file):
        intro = self.next_line(the_file)
        question = self.next_line(the_file)
        answers = ["","",""]
        for i in range(3):
            answers[i] = self.next_line(the_file)
        correct = self.next_line(the_file)
        if correct:
            correct = correct[0]
        incorrect = self.next_line(the_file)
        if incorrect:
            incorrect = incorrect[0]
        return intro, question, answers, correct, incorrect

    def open_file(file_name, mode):
        try:
            file_name = open(file_name, mode)
        except IOError as e:
            print("Unable to open the file ", file_name, ". Ending program.\n", e)
            input("\n\nPress the enter key to exit.")
            sys.exit()
        else:
            return file_name


class AngryOldLady(FileReader):

    #reads the quiz information from a file, adds it to a list, and 
    def __init__(self, fileName):
        try:
            quizFile = open(fileName, "r")
        except IOError as e:
            print("Unable to open the file AngryQuiz.txt. Ending program.\n", e)
            input("\n\nPress the enter key to exit.")
            sys.exit()
        self.beginDialog = super().next_line(quizFile)
        self.endDialog = super().next_line(quizFile)
        self.gEnding = super().next_line(quizFile)
        self.bEnding = super().next_line(quizFile)
        self.goodPoints = int(0)
        self.badPoints = int(0)
        self.totalPoints = int(0)
        self.quizBlock = []
        self.line = []
        intro, question, answers, correct, incorrect = super().next_block(quizFile)
        while intro:
            self.line.append(intro)
            self.line.append(question)
            self.line.append(answers)
            self.line.append(correct)
            self.line.append(incorrect)
            self.quizBlock.append(self.line)
            intro, question, answers, correct, incorrect = super().next_block(quizFile)
            self.line = []

    def getBeginDialog():
        return self.beginDialog

    def getendDialog():
        return self.endDialog

    
    def getQuestion(self):
        question = random.choice(self.quizBlock)
        tmp = self.quizBlock.index(question)
        self.quizBlock.pop(tmp)
        return question
    
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


class AnimalList(FileReader):
    def __init__(self):
        super().__init__()


    def buildList(file_name):
        the_file = super().open_file(AnimalList, file_name, "r")
        self.__list = []
        aName, aDesc, aGood, aBad = super().next_block(file_name)

        while aName:
            animal = Animal(aName, aDesc, aGood, aBad)
            __list.append(animal)
            aName, aDesc, aGood, aBad = next_block(filename)
        the_file.close()
        return __list


    @classmethod
    def next_block(self, fileName):
        name = super().next_line(self, fileName)
        description = super().next_line(self, fileName)
        good = super().next_line(self, fileName)
        bad = super().next_line(self, fileName)
        return name, description, good, bad
