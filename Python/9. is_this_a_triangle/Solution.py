def is_triangle(a, b, c):
    #there is a condition where 2 sides added may be >= to the third side. This was not considered in this solution.
    #otherwise any 2 sides added must be greater than the third
    #look up conditions for existence of a triangle -> https://en.wikipedia.org/wiki/Triangle#Condition_on_the_sides
    isTriangle = (a+b > c) * (b + c > a) * (a+c > b)
    return isTriangle
