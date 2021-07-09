"""
Longest Alternating Substring

Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.
Examples

longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.

Notes

The minimum alternating substring size is 2.
"""

def even(number):
    if number == 0:
        return True
    return odd(number - 1)

def odd(number):
    if number == 0:
        return False
    return even(number - 1)

def longest_substring(text:str) -> str:
    res = list()
    str_res = str()
    for num in list(map(int,text)):
        if len(str_res) == 0:
            str_res += str(num)
        else:
            if odd(int(str_res[-1])) == odd(num):
                res.append(str_res)
                str_res = str(num)
            else:
                str_res += str(num)
    if len(str_res) != 0:
        res.append(str_res)
    else:
        pass
    return max(res, key=len)
