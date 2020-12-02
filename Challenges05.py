#The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

#Create a function that takes a string and applies the Atbash cipher to it.

##Examples
'''atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"'''

##Encryption
#The Atbash cipher is a particular type of monoalphabetic cipher formed by taking the alphabet (or abjad, syllabary, etc.) and mapping it to its reverse, so that the first letter becomes the last letter, the second letter becomes the second to last letter, and so on. For example, the Latin alphabet would work like this:

#Plain	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
#Cipher	Z	Y	X	W	V	U	T	S	R	Q	P	O	N	M	L	K	J	I	H	G	F	E	D	C	B	A

#Due to the fact that there is only one way to perform this, the Atbash cipher provides no communications security, as it lacks any sort of key. If multiple collating orders are available, which one was used in encryption can be used
#as a key, but this does not provide significantly more security, considering that only a few letters can give away which one was used.


##Notes
#Capitalisation should be retained.
#Non-alphabetic characters should not be altered.

plain = "A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z".split(' ')
cipher ="Z z Y y X x W w V v U u T t S s R r Q q P p O o N n M m L l K k J j I i H h G g F f E e D d C c B b A a".split(' ')

def atbash(txt):
    cipherTxt = ''
    for char in txt:
        if char in plain:
            cipherChar = cipher[plain.index(char)]
            cipherTxt += cipherChar
        else:
            cipherTxt += char
    return cipherTxt
