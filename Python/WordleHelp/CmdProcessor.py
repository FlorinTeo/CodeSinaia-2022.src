###
# Class CmdProcessor is in charge of implementing all commands supported by WordleHelp
from WordChecker import WordChecker

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

    def processAdd(self, args = None):
        print("Process command 'add'")

    def processMatch(self, args = None):
        print("Process command 'match'")
    
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
    cmdP.processHelp()