#Disarium Number

#A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

#Create a function that determines whether a number is a Disarium or not.

##Examples

    #is_disarium(75) ➞ False
    ## 7^1 + 5^2 = 7 + 25 = 32

    #is_disarium(135) ➞ True
    ## 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

    #is_disarium(518) ➞ True

    #is_disarium(8) ➞ True

#Notes

    #Position of the digit is 1-indexed.

def is_disarium(n):
    if len(str(n)) == 1:
        return True
    else:
        result = 0
        a = 0
        for i in str(n):
            a += 1
            result += int(i)**a
        if result == n:
            return True
        else:
            return False