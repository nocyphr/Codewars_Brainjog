def solution(s):
    # branchless add a '_' to the end if the len of the string is not even
    sEven = s + (len(s) % 2 != 0) * '_'

    # join every nth element with every n + 1th element into a tuple via zip
    pairZip = zip(sEven[::2], sEven[1::2])

    # since there will always only be pairings of 2 we just do a list comprehension on the zip by joining both strings of the current tuple we are iterating over
    return [i[0] + i[1] for i in pairZip]