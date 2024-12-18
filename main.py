print("Hey, Welcome to my basic calculator")

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "undefined"
def times(a, b):
    return a * b



while True:
    
    operator = input("enter 'add' for addition, 'sub' for subtraction, 'div' for division and 'times' for multiplication: \n").lower()
    
    if operator == "exit":
        print("Goodbye!")
        break
    try:
        a = float(input("Enter your first number \n"))
        b = float(input("enter your second number \n"))
    except ValueError:
        print("Invalid input!, please enter a number")
    
    if operator == "add":
        print(add(a, b))
    elif operator == "div":
        print(div(a, b))
    elif operator == "sub":
        print(sub(a, b))
    elif operator == "times":
        print(times(a, b))
    else:
        print("invalid operator! try again")