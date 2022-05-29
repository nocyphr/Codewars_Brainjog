def friend(x):
    #List comprehension for all elements in x with len = 4
    friendsList = [i for i in x if len(i) == 4]
    return friendsList