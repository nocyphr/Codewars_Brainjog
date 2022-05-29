def sort_array(source_array):
    # init helper vars. n is a countervariable for the elements of odd numbers
    n = 0
    sortedArr = []

    # get odd numbers from parentlist and sort ascending
    oddNumbers = [i for i in source_array if i % 2 != 0]
    oddNumbers.sort()

    # loop over parentlist. if found number is odd, add the smallest element from oddNumbers that has not been added yet.
    # otherwise just copy the even number over
    for i in source_array:

        if i % 2 != 0:
            sortedArr.append(oddNumbers[n])
            n += 1

        else:
            sortedArr.append(i)

    return sortedArr