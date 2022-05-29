def move_zeros(array):
    # first get the number n of occurences of 0
    n = array.count(0)

    # clean array of all 0s
    array = [_ for _ in array if _ != 0]

    # lastly append 0 n times to the array
    for _ in range(n):
        array.append(0)

    return array