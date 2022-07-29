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
    # _wordsDb: the "database" of words is a dictionary of words (keys)
    #           mapped to their frequencies (values)

    ###
    # Class constructor
    def __init__(self):
        self._wordChecker = WordChecker()
        self._wordsDb = {}

    def processHelp(self):
        print("process command 'help'")

    def processAdd(self, args = None):
        print("Processing command 'add'...")
        input = args[4:]
        textread = Scraper(input)
        words = textread._text.split()
        length = len(self._wordsDb)
        for x in words:
            word = x.lower()
            if len(word)==5 and word.isalpha() == True:
                if word in self._wordsDb: self._wordsDb[word]=self._wordsDb[word]+1
                else: self._wordsDb[word]=1
        print("Added {count} words to dictionary.".format(count=len(self._wordsDb)-length))

    def processMatch(self, args = None):
        arr = args.split()
        hasHint = len(arr) > 1
        if hasHint:
            self._wordChecker.update(arr[1])

        count = 5
        for word in self._wordsDb.keys():
            if not hasHint or self._wordChecker.check(word):
                print(word)
                count -= 1
                if count == 0:
                    break
    
    def processPrint(self, args = None):
        print('\033[96m')
        for key, value in self._wordsDb.items():
            print("Word: ",key,"Appearence: ",value)
        print("\x1b[0m")

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