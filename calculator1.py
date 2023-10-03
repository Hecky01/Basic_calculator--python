#This is console app calculator which operates with: +, -, *, /

number1 = 0
number2 = 0
userinput = ''
action = ''

def actions():
    if action == '+':
        print(number1 + number2)
    elif action == '-':
        print(number1 - number2)
    elif action == '/':
        print(number1 / number2)
    elif action == '*':
        print(number1 * number2)
    
while userinput != 'no':
    number1 = float(input('Please enter first number\n'))
    action = input('What action would you like to make?\nAvailable are:\n + - * / \n')
    number2 = float(input('Please enter second number\n'))

    try:
        actions()
    except:
        print('error appears')
    userinput = str(input('Would you like to start over? yes/no ... \n'))

input('\nPress enter to exit...')
