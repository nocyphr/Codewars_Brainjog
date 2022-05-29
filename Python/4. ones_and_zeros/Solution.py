def binary_array_to_number(arr):
    # arr to string
    arrString = ''.join(str(i) for i in arr)
    # arrString to int
    theInt = int(arrString, 2)
    #done
    return theInt