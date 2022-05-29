def row_sum_odd_numbers(n):
    t1 = ((n - 2) / 2) * (n + 1) * 2 + 3
    t2 = t1 + 2 * n - 2
    theSum = (n / 2) * (t1 + t2)
    return theSum

    # arithmetic series to get number of elements from row 2 to row n - 2
    # multiply by 2 and add 1 to get last element of row n - 1
    # calculate first and last element in row n
    # arithmetic series to get sum of elements in row n between first and last element without a for loop.