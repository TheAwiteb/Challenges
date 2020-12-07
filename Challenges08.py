#In BlackJack, cards are counted with -1, 0, 1 values:

#2, 3, 4, 5, 6 are counted as +1
#7, 8, 9 are counted as 0
#10, J, Q, K, A are counted as -1
#Create a function that counts the number and returns it from the list of cards provided.

#Examples
'''count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5'''

##Notes
#String inputs will always be upper case.
#You do not need to consider case sensitivity.
#If the argument is empty, return 0.
#No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".


def count(deck):
    n = 0
    numList = []
    n1 = [2,3,4,5,6]
    n0 = [7,8,9]
    n_1 = [10,'J','Q','K','A']
    if deck == []:
        return 0
    for x in deck:
        if x in n1:
            numList.append(1)
        elif x in n_1:
            numList.append(-1)
        elif x in n0:
            numList.append(0)
        else:
            pass
    for num in numList:
        n += num
    return n
