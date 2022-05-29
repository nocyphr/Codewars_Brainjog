def descending_order(num):
    # int to string to list
    strList = list(str(num))

    # sort it descending
    strList.sort(reverse=True)

    # rejoin elements together and convert resulting string back to int
    return int(''.join(strList))