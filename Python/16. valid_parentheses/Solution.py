def valid_parentheses(s):
    theSum = 0
    for c in s:
        theSum += (c == '(') + (c == ')')*-1
        if theSum < 0:
            return False
    return theSum == 0
