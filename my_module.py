def calc(a,b):
    return a + b


def sub(a, b):
    return a - b


def multi(a,b):
    return a * b


def devision(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("can`t divide by 0")