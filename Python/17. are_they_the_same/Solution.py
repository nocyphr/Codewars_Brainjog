def comp(a1, a2):
    # check if arrays are None
    if None not in [a1, a2]:
        # square all elements in a1
        a1 = [i ** 2 for i in a1]

        # sort both to potentially make them equal
        a1.sort()
        a2.sort()

    return (a1 == a2)