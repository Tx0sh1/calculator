print("Hey, Welcome to my basic calculator")


operator = input("enter 'add' for addition, 'sub' for subtraction, 'div' for division and 'times' for multiplication: \n")



a = float(input("Enter your first number \n"))
b = float(input("enter your second number \n"))


def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def div(a, b):
    if b != 0:
        return a / b
    else:
        print("cannot divide by 0")
def times(a, b):
    return a * b


if operator == "add":
    print(add(a, b))
elif operator == "div":
    print(div(a, b))
elif operator == "sub":
    print(sub(a, b))
elif operator == "times":
    print(times(a, b))
