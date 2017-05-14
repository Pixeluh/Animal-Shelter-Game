import sys
from FileReader import FileReader
class SaveAndLoader(object):
    def save(row, pPos, pGood, pBad):
        fileName = FileReader.open_file("save.txt", "w")
        fileName.write(str(row) + "\n")
        fileName.write(str(pPos) + "\n")
        fileName.write(str(pGood) + "\n")
        fileName.write(str(pBad) + "\n")
        fileName.close()

    @classmethod
    def load(self):
        fileName = FileReader.open_file("save.txt", "r")
        row = FileReader.next_line(self, fileName)
        character = FileReader.next_line(self,fileName)
        gPoints = FileReader.next_line(self, fileName)
        bPoints = FileReader.next_line(self,fileName)
        fileName.close()
        return row, character, gPoints, bPoints
