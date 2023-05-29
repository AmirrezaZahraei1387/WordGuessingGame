"""this code file will use the words to select one of them 
for the game. it will select the first word of the csv file
and then push it at the end of the file."""

import csv
import data.data_path_reader 


class ChooseWord:
    """this class choose word!"""

    def __init__(self):
        self.languages, self.paths = data.data_path_reader.open_file()

    def open_csv(self, path_index):
        """this method will open the csv. the path_index
        is the index of the path in self.paths list"""

        with open(self.paths[path_index], mode = 'r', encoding="utf-8") as file:
            read = csv.reader(file)
            read = list(read)
        
        return read

    def write_csv(self, data, path_index):
        """this method will get """
        with open(self.paths[path_index], mode='w', encoding='utf-8') as file:
            write=csv.writer(file)
            write.writerows(data)

    def pick(self, language:str):
        """this method will pick a word from the data.
        if the output of method was False it means language is
        not supported"""

        if language not in self.languages:
            return False # means that the language is not  supported
        
        index = self.languages.index(language)
        data = self.open_csv(index)

        word = data[1] # this will get the first word of the 
        # data. it uses 1 because the first index is occupied 
        # b the field

        data.append(data[1])
        data.pop(1)

        self.write_csv(data, index)

        return word





    

    


