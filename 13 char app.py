''' Michael Xu '''
'''Problem: Write a program that takes an input string and prints it as multiple lines of text such that no line of text
 is greater than 13 characters and words are kept whole.  Add commentary which explains thought process.  It is very
 important to explain your work through your commentary.'''

import re

testString = "Four score and seven years ago our congratulations fathers brought forth upon this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal"
remainingString=testString+" " #added a space to the end to ensure there's a final space
currentLine = ""
LINE_LENGTH = 13

#helper methods start here.
def nextSpaceDistance(inputString):
    index=inputString.find(' ')
    return index
def flushCurrentLine(): #this helper method will reduce duplicate code by pulling common functionality into one function.
    # this makes the code easier to maintain since you only need to make changes in one place to affect all three places
    #  that this function gets used
    global remainingString #needs to be global in order to operate on the parent variable. I could pass it in as a variable as an alternative.
    global currentLine
    print currentLine #flushes out the current line to the console
    currentLine = "" #clears out the current line variable. it's global, so we don't need to worry about scope.
    if remainingString.startswith(" "): #we need to remove any leading spaces in the remaining string, since we don't
        # want to print out anything with spaces in the front. We want to do this now instead of later, because leading
        # spaces can affect line length.
        remainingString = re.sub("^ +", "", remainingString,1)  # this will remove any leading spaces, handles any
        # number of leading spaces, and only the head.

#main section starts here
while len(remainingString)>1:
    nextIndex=nextSpaceDistance(remainingString[1:])+1 #the +1 is because we start counting from 0
    if nextIndex >= LINE_LENGTH: #if the word itself is larger than 13, such as a word like "congratulations", a
        # fairly common word with a length of 15, we need to handle this case.
        #I am assuming requirememnts here. Normally, I'd ask the stakeholders what the process should do in this case,
        #but since this is a programming assignment, I'm just going to make my own requirements here.
        #words longer than 13 will be put into their own line, with hyphens seperate the split parts of the word.
        flushCurrentLine()
        remainingString=remainingString[0:LINE_LENGTH-2]+"- "+remainingString[LINE_LENGTH-2:] #i'm adding the hyphen
        # and adding a space seperator so it'll now be counted as a seperate word.
    elif nextIndex+len(currentLine)>=LINE_LENGTH:  # if the next word will push us over the line limit, then flush out
        # the current line and start over again with the remaining words.
        flushCurrentLine()
    else: #if the next word will not push us over the line limit, then add the next word to our current line.
        currentLine = currentLine+remainingString[0:nextIndex]
        remainingString = remainingString[nextIndex:]
flushCurrentLine() #this flushes out the last line. during the loop, lines only get flushed out if the next word will
# make the current one too long. for the final case, there is no word to push the line to 13 characters, so we need to
#  manually flush out the last line.

