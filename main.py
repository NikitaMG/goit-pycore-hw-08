import my_module
import sys
while True:
    first = int(input('write the first number: '))

    action = input('please chose the action (+ - * / %) :' )

    second = int(input('write the second number: '))

    result = None

    if action == '+':
        result = (my_module.calc(first,second))

    elif action == '-':
        result = (my_module.sub(first,second))

    elif action == '*':
        result = (my_module.multi(first,second))

    elif action == '/':
         try:
             result = (my_module.devision(first,second))
         except ZeroDivisionError:
             result = ("You can`t divide by 0")
    elif action == '%':
        result = (first % second)
    else:
        print('chose the correct action')

    print("result: ", result)
    try:
        with open('ForCalculator', 'a') as f:
            f.write(f"{first} {action} {second} = {result} \n")
    except IOError:
        print("sorry")
        break
    repeat = input('do u want to continue?').strip().lower()
    if repeat == 'yes':
        continue
    else:
        print('thank you')
        sys.exit()


