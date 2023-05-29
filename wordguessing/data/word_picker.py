"""this code file will use the words to select one of them 
for the game. it will select the first word of the csv file
and then push it at the end of the file."""

import csv
from data_path_reader import open_file


class ChooseWord:
    """this class choose word!"""

    def __init__(self):
        self.languages, self.paths = open_file()

    def open_csv(self, path_index):
        """this method will open the csv. the path_index
        is the index of the path in self.paths list"""

        with open(self.paths[path_index], mode = 'r', encoding="utf-8") as file:
            read = csv.reader(file)
            read = list(read)
        
        return read

    def write_csv(self, data, path_index):
        """this method will get """
        with open()
    

    

    


