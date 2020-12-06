'''Write a program that calculates the average salary of an indefinite number of employees.
1.  [  /1pt] The program should prompt the user to enter the salary of each employee

2.  [  /2pts] The program should also ask the user to enter if that employee is a male or female:
o  Create an error trap (validation loop) that validates whether the user entered a correct gender value (f or m). If not, keep prompting the user to enter a valid gender value until they do so.

3.  [  /1pt] The program should terminate when the user enters -1, instead of entering a valid salary.

4.  [  /3pts] After the user enters all employee salaries and genders,

o  Display the total number of male employees
o  Display the total number of female employees
o  Display the average salary of all employees'''

totalF = 0
totalM = 0
totalSalary = 0
loop = True
while loop:
    while True:
        try:
            salary = int(input('\nEnter employee salary: '))
            if salary < 0:
                loop = False
                print('\n---Resuls---\n')
                break
            totalSalary += salary
            break
        except ValueError:
            print('Enter salary just number..!')
    while loop:
        gender = input("Enter The employee's gender (m/f): ")
        if gender =='f':
            totalF += 1
            break
        elif gender == 'm':
            totalM += 1
            break
        else:
            print('Please enter gender m or f.!')

print(f"Total number of male employee's: {totalM}\nTotal number of female employee's: {totalF}")
print(f"Total employee's: {totalM + totalF}")

try:
    print(f"Average salary of all employee: {totalSalary /(totalM + totalF)}")
except ZeroDivisionError as z:
    print(z)
