def find_short(s):
    #split by spaces
    wordList = s.split()
    #get list of lengths of elements in the wordList
    lenList = [len(i) for i in wordList]
    #get smallest value from lenList
    return min(lenList)