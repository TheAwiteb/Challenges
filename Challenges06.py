#It's time to send and receive secret messages.

#Create a single function that takes a string or a list and returns a coded or decoded message.

#The first letter of the string, or the first element of the list represents the
#Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.


##Examples
'''dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
# H = 72, the difference between the H and e is 29 (upper- and lowercase).
# The difference between the two l's is obviously 0.

dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]'''

##Notes
#The input of the function will always be a string or a list with numbers.
def dif_ciph(input_):
    if type(input_) == str:
        listNum = []
        indexL = []
        for char in input_:
            indx = input_.index(char)
            if indx in indexL:
                num = ord(char) - ord(input_[indexL[-1]])
            else:
                if indx == 0:
                    num = ord(char)
                else:
                    num = ord(input_[indx]) - ord(input_[indx - 1])
            listNum.append(num)
            indexL.append(indx)
        return listNum

    elif type(input_) == list:
        text = ''
        charL = []
        for num in input_:
            try:
                int(num)
            except:
                return None

            if len(charL) == 0:
                char = chr(num)
            else:
                char = ord(charL[-1]) + num
                char = chr(char)
            charL.append(char)
            text += char
        return text
