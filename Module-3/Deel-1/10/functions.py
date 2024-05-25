def addition(num1: int, num2: int):
    return num1 + num2

def subtraction(num1: int, num2: int):
    return num1 - num2

def multiplication(num1: int, num2: int):
    return num1 * num2

def division(num1: int, num2: int):
    if num2 != 0:
        return num1 / num2
    else:
        return "Delen door nul is niet toegestaan"
###########################
def increment(num1: int):
    return num1 + 1

def decrement(num1: int):
    return num1 - 1

def double(num1: int):
    return num1 * 2

def halve(num1: int):
    return num1 / 2
###########################
def square(num1:int):
    return num1 ** 2

def cube(num1:int):
    return num1 ** 3

def square_root(num1:int):
    return num1 ** (1/2)

def cube_root(num1:int):
    return num1 ** (1/3)

def factorial(num1:int):
    if num1 == 0:
        return 1
    else:
        return num1 * factorial(num1 - 1)