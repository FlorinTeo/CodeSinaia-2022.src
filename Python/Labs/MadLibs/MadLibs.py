import os
import sys

try:

    ###
    # Simple implementation of the MadLibs game.
    # Script expects one command line argument, pointing to a text file on the disk
    # The text file is a sequence of lines, each being a sequence of words.
    # Words starting with "<" are placeholders to be filled in by the user.
    # ref: https://en.wikipedia.org/wiki/Mad_Libs

    # Get the file name of a MadLibs template file
    inFilePath = input("Enter the path to the input file> ")
    if not os.path.isfile(inFilePath):
        raise Exception(f"File {inFilePath} cannot be located!")

    # Initialize a string variable to hold the output of the game
    # then read the input file line by line and word by word
    outputText = ''
    inputText = open(inFilePath).readlines()
    for line in inputText:
        words = line.split()
        for word in words:
            iStart = word.find("<")
            # if word contains "<", extract the placeholder text
            # ask the user for its substitute and reconstruct the word
            if iStart >= 0:
                iEnd = word.find(">")
                if iEnd == -1:
                    raise Exception("Madlib file is corrupted")
                prefix = word[:iStart]
                suffix = word[iEnd+1:]
                question = word[iStart+1:iEnd]
                answer = input(f"{question}?> ")
                word = f"{prefix}{answer}{suffix}"
            outputText += f" {word}"
        outputText += "\n"

    # print the resulting text
    print()
    print(outputText)
    # output the resulting text in a file.
    # the output file has the same name as the input file, appended with the "_final" suffix
    outFilePath = (inFilePath + "_final") if (inFilePath.rfind(".", ) == -1) else (inFilePath.replace(".", "_final."))
    with open(outFilePath, "w") as outFile:
        outFile.write(outputText)
        outFile.close()

    # int x = (y > 10) ? y - 10 : y;
except Exception as e:
    print("Encountered error!!!")
    print(e)