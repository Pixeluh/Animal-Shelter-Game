import Animal, FileReader

class AnimalList(FileReader):
    def buildList(file_name):
        the_file = open_file(file_name, "r")
        __list = []
        aName, aDesc, aGood, aBad = next_block(file_name)

        while aName:
            animal = Animal(aName, aDesc, aGood, aBad)
            __list.append(animal)
            aName, aDesc, aGood, aBad = next_block(filename)

        return __list

    def next_block(self, fileName):
        name = next_line(fileName)
        description = next_line(fileName)
        good = next_line(fileName)
        bad = next_line(fileName)
        return name, description, good, bad
