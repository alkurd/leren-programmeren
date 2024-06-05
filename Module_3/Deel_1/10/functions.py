#1
def addition(num1: int, num2: int):
    return num1 + num2

#2
def subtraction(num1: int, num2: int):
    return num1 - num2

#3
def multiplication(num1: int, num2: int):
    return num1 * num2

#4
def division(num1: int, num2: int):
    if num2 != 0:
        return num1 / num2
    else:
        return "Delen door nul is niet toegestaan"
###########################
#5
# def increment(num1: int):
#     return num1 + 1

# #6
# def decrement(num1: int):
#     return num1 - 1

# #7
# def double(num1: int):
#     return num1 * 2

# #8
# def halve(num1: int):
#     return num1 / 2
###########################
#9
def square(num1:int):
    return num1 ** 2

#10
def cube(num1:int):
    return num1 ** 3

#11
def square_root(num1:int):
    return num1 ** (1/2)

#12
def cube_root(num1:int):
    return num1 ** (1/3)

#13
def factorial(num1:int):
    if num1 == 0:
        return 1
    else:
        return num1 * factorial(num1 - 1)


