#A block sequence in three dimensions. We can write a formula for this one:
#Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.

#Examples
'''blocks(1) ➞ 5

blocks(5) ➞ 39

blocks(2) ➞ 12'''
##Notes
#Step 0 obviously has to return 0.
#The input is always a positive integer.
#Check the Resources tab for a video on finding quadratic sequences.


# Explanation of the sequence "htn"   "https://www.s-cool.co.uk/gcse/maths/sequences/revise-it/the-nth-term"
def blocks(step):
      #a       #b     #c
    "0.5n**2 + 5.5n - 1"
    if step != 0:
        a = 0.5*step ** 2
        b = 5.5 * step
        c = -1
    else:
        return 0
    return int(a + b + c)

a = int(input('>: '))
print(blocks(a))
