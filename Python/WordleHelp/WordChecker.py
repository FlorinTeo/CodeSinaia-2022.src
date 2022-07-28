###
# Class owning the set of hints given in the course
# of playing one game of Wordle
from re import L


class WordChecker:
    ###
    # Class fields
    # _gray: set of "gray" characters.
    #        characters in this set should not be present in word
    # _green: array of 5 characters, initially all None
    #        a valid character in position i in this array should
    #        be found on the same position in the word being checked.
    # _yellow: dictionary of characters (key) mapped to an array of
    #        5 booleans (value). A value True in that array indicates the
    #        the character was flagged as "yellow" for that position in
    #        a previous hint
    # _allHints: a list of all hints available so far
    #        This is only used for printing purposes

    ###
    # Class constructor:
    def __init__(self):
        self._gray = set()
        self._green = [None, None, None, None, None]
        self._yellow = {}
        self._allHints = []

    ###
    # Updates the internal state of the checker with a new hint
    def update(self, hint):
        #hint looks like "~ST+AIR"
        lastMarker = None
        iChar = 0
        for c in hint:
            if c == '+' or c == '~':
                lastMarker = c
                continue
            if lastMarker == None:
                if c not in self._green and c not in self._yellow.keys():
                    self._gray.add(c)
            elif lastMarker == '+':
                self._green[iChar] = c
                self._gray.discard(c)
            elif lastMarker == '~':
                if c not in self._yellow.keys():
                    self._yellow[c] = [False, False, False, False, False]
                self._yellow[c][iChar] = True
                self._gray.discard(c)
            iChar += 1
            lastMarker = None
        self._allHints.append(hint)

     ###
     # Checks whether a given word matches all known hints
    def check(self, word):
        print(f"TODO: WordChecker testing if '{word}' verifies all known hints.")
        return True
        
    ###
    # Returns a string representation of the entire object
    def __str__(self):
        for hint in self._allHints:
            print(hint)

###
# WordChecker test code
if __name__ == "__main__":
    # creates a test WordChecker object and run through its methods
    wordChecker = WordChecker()
    wordChecker.update("SOR~ES")
    wordChecker.update("T~EEN+E")
    print(wordChecker)