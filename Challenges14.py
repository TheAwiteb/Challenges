#Combinations

#Create a function that takes a variable number of arguments, each argument representing the number of items in a group, 
#and returns the number of permutations (combinations) of items that you could get by taking one item from each group.

##Examples

    #combinations(2, 3) ➞ 6

    #combinations(3, 7, 4) ➞ 84

    #combinations(2, 3, 4, 5) ➞ 120

##Notes

    #Don't overthink this one.
    #Input may include the number zero.


def combinations(*items):
    result = 1
    for num in items:
        if num > 0:
            result *= num
    return result