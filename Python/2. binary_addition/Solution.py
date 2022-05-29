def add_binary(a,b):
    #this solution does not account for varying inputs. Fails on any type other than int
    theSum = sum((a,b))
    theBin = format(theSum, 'b')
    return theBin