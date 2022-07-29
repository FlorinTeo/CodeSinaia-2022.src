class TrieNode:

    ###
    # Class fields:
    # _char: the character value held by this node
    # _counter: counts the number of times this node has been visited
    # _children: links to the child nodes keyed by their charater

    def __init__(self, char = ""):
        self._char = char
        self._counter = 0
        self._children = {}

    def addWord(self, word, frequency = 1):
        self._counter += frequency
        if not word:
            return
        nextChar = word[0]
        nextWord = word[1:]
        if nextChar not in self._children:
            self._children[nextChar] = TrieNode(nextChar)
        self._children[nextChar].addWord(nextWord, frequency)

    def printTree(self, prefix = ""):
        print(f"{prefix}{self._char} : {self._counter}")
        for child in self._children.keys():
            self._children[child].printTree(f"{prefix}{self._char}")

    def traceWord(self, word):
        pass

if __name__ == "__main__":
    root = TrieNode()
    root.addWord("CARDS", 2)
    root.addWord("CHAOS")
    root.addWord("CHARM")
    root.addWord("CARES")
    root.addWord("CHESS")
    root.printTree()
    root.traceWord("CARES")