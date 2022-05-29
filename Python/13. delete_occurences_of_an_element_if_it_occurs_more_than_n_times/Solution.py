def delete_nth(order,max_e):
    #enumerate the list to keep track of the index. Then check for each element up to the current element
    #if the number of occurences is <= maximum allowed. Slap it into a list comprehension and you are done.
    return [element for i, element in enumerate(order) if order[:i+1].count(order[i]) <= max_e]