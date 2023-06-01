"""this file impelements the easy logic of the program"""
from data import ChooseWord
import random

class WGGame(ChooseWord):
    """this is a class that  impelements the logic of the wordguessing game"""

    __word:list = []
    len_word:int = 0
    __giveword:list = []
    __hardness:int = 0

    def __init__(self):
        super().__init__()

    def def_word(self, lang):
        """this method will choose a word based on the givven language
        and then it will parse it  into a list of words"""
        word = self.pick(language=lang)
        lword = []
        for letter in word:
            lword.append(letter)

        self.__word = lword
        self.len_word = len(self.__word)

    @property
    def hardness(self):
        return self.__hardness
    
    @hardness.setter
    def hardness(self, other):

        if other == "HARD":
            self.__hardness=random.randint(self.len_word+5, self.len_word+10)

        elif other == "INTERMEDIATE":
            self.__hardness=random.randint(self.len_word*2, self.len_word*3)
        
        elif other =="EASY":
            self.__hardness=random.randint(self.len_word**2, self.len_word**2+20)

        else:
            raise ValueError("the givven input must be(HARD, INTERMEDIATE, EASY)")
    
    @property
    def giveword(self):
        return self.__giveword
    
    @giveword.setter
    def giveword(self, other:list):

        if len(other) == self.len_word:
            self.__giveword = other
        else:
            raise TypeError("the givven input must have the same length as thr picked word")
        
    def setAsDefault(self):
        """this method will set all the variables"""
        self.__word = []
        self.__giveword = []
        self.__hardness = 0
        self.len_word = 0

    

        
    

    

