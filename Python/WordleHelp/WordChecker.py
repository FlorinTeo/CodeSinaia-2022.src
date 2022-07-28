###
# Class owning the set of hints given in the course
# of playing one game of Wordle
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
        '''
        keep track of lastMarker (one of '+' or '~'). Initially None
        for each character in hint
            if character is a marker
               save it in lastMarker and continue
            otherwise we have a valid character ch
            if lastMarker is None
               add ch to the _gray set, if it was not previously either green or yellow
            otherwise, if lastMarker is '+'
               add ch to the green set
            otherwise if lastMarker is '~'
               add ch to the yellow set if not already in there
               and set its position in the map to True
            set lastMarker to None (since this was a character, not a marker)
        add the hint to _allHints 
        '''

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
    wordChecker.update("~S+TAIR")
    print(wordChecker.check("TOLLS"))
    print(wordChecker)