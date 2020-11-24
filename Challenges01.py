import numpy
import random
from time import sleep

def generateNumbers(numbers):
    'It generates a number and puts it in List so that it does not repeat again'
    while True:
        number = numpy.arange(smallNum,largeNum).tolist()
        number = number[int(len(number) / 2)]
        if number in numbers:
            pass
        else:
            numbers.append(number)
            break
    return number
largeNum = 100
smallNum = 1
attempts = 10
numbers = []
print('Think number 1-100')
sleep(4)
while True:
    for i in range(attempts):
        print(f"\n\nOk i have {attempts} attempts")
        number = generateNumbers(numbers)
        print(f'yor number between {smallNum} and {largeNum}')
        print(f'\nI think is {number}')
        print(f"   [1]your number is greater {number}\n   [2]your number is younger {number}\n   [3]Yes is {number}")
        choice = input("\nChoice 1 or 2 or 3: ")
        if choice == '1':
            smallNum = number
        elif choice == '2':
            largeNum = number + 1
        elif choice == '3':
            print('Yes i win..!')
            break
        else:
            pass
        attempts -= 1
    again = input('play again? y/n: ')
    if again == 'y':
        largeNum = 100
        smallNum = 1
        attempts = 10
        numbers = []
    else:
        break
