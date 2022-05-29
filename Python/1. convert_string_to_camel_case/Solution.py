import re
def to_camel_case(text):
    #split on anything not a letter or number
    splitText = re.split('[^a-zA-Z0-9]',text)
    #init Var for joined Text and set to empty string
    joinedText = ''
    #loop over split text
    for s in splitText:
        #branchless - if empty string, return current element, if not, return capitalized element
        joinedText += (joinedText == '')*s + (joinedText != '')*s.title()
    return joinedText
