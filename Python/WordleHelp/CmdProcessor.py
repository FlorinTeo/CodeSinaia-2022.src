class CmdProcessor:

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

if __name__ == "__main__":
    cmdP = CmdProcessor()
    cmdP.processHelp()
    print(cmdP.semnatura)
    cmdP2 = CmdProcessor()
    cmdP2.processAdd()
    print(cmdP2.semnatura)
    print(cmdP.semnatura)