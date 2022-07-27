###
# Class owning the set of hints given in the course
# of playing one game of Wordle
class WordChecker:

    ###
    # Class constructor:
    def __init__(self):
        print(f"TODO: WordChecker is initialized")

    ###
    # Updates the internal state of the checker with a new hint
    def update(self, hint):
        print(f"TODO: WordChecker adding the hint: '{hint}'.")

     ###
     # Checks whether a given word matches all known hints
    def check(self, word):
        print(f"TODO: WordChecker testing if '{word}' verifies all known hints.")
        return True
        
    ###
    # Returns a string representation of the entire object
    def __str__(self):
        return f"TODO: WordChecker internal state."

###
# WordChecker test code
if __name__ == "__main__":
    # creates a test WordChecker object and run through its methods
    wordChecker = WordChecker()
    wordChecker.update("some hint")
    print(wordChecker.check("some word"))
    print(wordChecker)