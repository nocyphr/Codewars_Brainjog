def count_bits(n):
    #convert number to binary and binary to string
    theBin = str(format(n, 'b'))
    #use count function to get number of 1s in the string
    return theBin.count('1')