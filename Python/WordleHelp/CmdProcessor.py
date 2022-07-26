class CmdProcessor:
    semnatura = "x"

    def processHelp(self):
        self.semnatura = "help"
        print("process command 'help'")
        self.processAdd()

    def processAdd(self, args = None):
        self.semnatura = "add"
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