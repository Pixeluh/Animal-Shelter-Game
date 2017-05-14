#from FileReader import FileReader
#from FileReader import AngryOldLady
from Animal import Animal
#from FileReader import AnimalList
from FileReader import *
import random
from SaveAndLoader import *

lady = AngryOldLady("AngryQuiz.txt")
print ("Good" + str(lady.getGoodPoints()))
print ("Bad" + str(lady.getBadPoints()))
lady.addBad()
lady.addGood()
quest = lady.getQuestion()
for i in range(5):
    intro = quest[0]
    print (intro)
    question = quest[1]
    print (question)
    for i in quest[2]:
        print ( i )
    correct = quest[3]
    print (correct)
    incorrect = quest[4]
    print (incorrect)
    quest = lady.getQuestion()
    input ("Press enter to continue")
print (lady.quizBlock)



print ("Good" + str(lady.getGoodPoints()))
print ("Bad" + str(lady.getBadPoints()))
animal = Animal("Spot", "A good boy", "pets", "spray bottle")
print (animal.getName())
print (animal.getDescription())
print (animal.getGood())
print (animal.getBad())

#build the list of animals
animalList = []
file = FileReader.open_file("Animals.txt","r")
name, description, good, bad = AnimalList.next_block(file)
while name:
    print (name + description + good + bad)
    animal = Animal(name, description, good, bad)
    animalList.append(animal)
    name, description, good, bad = AnimalList.next_block(file)
file.close()

#choose a random animal from the list
for i in range(10):
    temp = (random.choice(animalList))
    print (temp)
    animalList.remove(temp)

SaveAndLoader.save(10, 5, 10)
pPos, pGood, pBad = SaveAndLoader.load()
print (pPos)
print (pGood)
print (pBad)
           
#aList = AnimalList()
#animalList = AnimalList.buildList("Animals.txt")
