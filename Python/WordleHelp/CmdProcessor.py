###
# Class CmdProcessor is in charge of implementing all commands supported by WordleHelp
from typing import Dict
from WordChecker import WordChecker
from Scraper import Scraper


class CmdProcessor:
    ###
    # Class fields
    # _wordChecker: the "engine" in charge of storing and using all hints
    #               used for verifying words from the database

    ###
    # Class constructor
    def __init__(self):
        self._wordChecker = WordChecker()

    def processHelp(self):
        print("process command 'help'")

    def processAdd(self, args = None, dict : Dict = {}):
        print("Processing command 'add'...")
        input = args[4:]
        textread = Scraper(input)
        words = textread._text.split()
        length = len(dict)
        for x in words:
            word = x.lower()
            if len(word)==5 and word.isalpha() == True:
                if word in dict: dict[word]=dict[word]+1
                else: dict[word]=1
        print("Added {count} words to dictionary.".format(count=len(dict)-length))
        return dict

    def processMatch(self, args = None, dict = {}):
        arr = args.split()
        hasHint = len(arr) > 1
        if hasHint:
            self._wordChecker.update(arr[1])

        count = 5
        for word in dict.keys():
            if not hasHint or self._wordChecker.check(word):
                print(word)
                count -= 1
                if count == 0:
                    break
        '''
        if hint string exists
            self._wordChecker.update(hint)

        for each word in database:
            if self._wordChecker.check(word):
                print(word)
        '''
    
    def processReset(self, args = None):
        print("Process command 'reset'")

    def processStats(self, args = None):
        print("Process command 'stats'")

    def processConfig(self, args = None):
        print("Process command 'config'")

###
# CmdProcessor test code
if __name__ == "__main__":
    cmdP = CmdProcessor()
    d = cmdP.processAdd("add Python\\WordleHelp\\words.txt")
    cmdP.processMatch("match", d)
    cmdP.processMatch("match TERM~S", d)
    cmdP.processMatch("match ~ST+AIR", d)