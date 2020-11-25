#Write a function that accepts the width and height (m, n) and an optional proc s and generates a list with m elements. Each element is a string consisting of either:
#The default character (hash #) repeating n times (if no proc is given).
#The character passed in through the proc repeating n times.

##Notes
#You can set a value for the parameter when creating the function e.g. def func(x = 3)

#Examples
'''make_rug(3, 5) ➞ [
  "#####",
  "#####",
  "#####"
]

make_rug(3, 5, '$')  ➞ [
  "$$$$$",
  "$$$$$",
  "$$$$$"
]

make_rug(2, 2, 'A')  ➞ [
  "AA"
  "AA"
]'''

def make_rug(length = 5 , width = 3, char='#'):
     list_rug = []
     for le in range(length):
          for wi in range(width):
              string = char * width
          list_rug.append(string)
     return list_rug

leng = int(input('length: '))
wid = int(input('width: '))
cr = input("char: ")
a = make_rug(leng,wid,cr)
print(str(a).replace(' ', '\n').replace('[','\n').replace(']','\n'))
