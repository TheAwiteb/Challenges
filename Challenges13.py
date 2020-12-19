#*Encode and decode Morse*#


char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def encode_morse(message):
    morse = ''
    for char in message.upper():
        if char in char_to_dots:
            morse += char_to_dots[char] +'/'
        else:
            morse += char
    return morse.strip('/')

def decode_morse(morse):
    message = ''
    for m in morse.split('/'):
        for key,val in char_to_dots.items():
            if val == m:
                message += key
    return message


#print(decode_morse('...././.-../.--./ /--/./ /-.-.--'))

#print(encode_morse("HELP ME !"))