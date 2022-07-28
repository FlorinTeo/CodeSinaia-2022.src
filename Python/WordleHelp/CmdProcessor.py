###
# Class CmdProcessor is in charge of implementing all commands supported by WordleHelp
import os
import pyperclip
import requests
from WordChecker import WordChecker

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

    ###
    # Processes the command 'add': loading a file containing
    # records of words into the internal self._wordsDb
    def processAdd(self, args = None):
        source = args.split()[1]
        if not os.path.isfile(source):
            raise Exception(f"File {source} not found!")
        lines = open(source, "r").readlines()
        count = 0
        for line in lines:
            record = line.split()
            self._wordsDb[record[0].lower()] = int(record[1])
            count += 1
        print(f"Added {count} words to the database!")

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
    cmdP.processAdd("add Python\\WordleHelp\\words.txt")
    cmdP.processMatch("match")
    cmdP.processMatch("match TERM~S")
    cmdP.processMatch("match ~ST+AIR")