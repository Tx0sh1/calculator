print("Hey, Welcome to my basic calculator")

operator = input("enter 'add' for addition, 'sub' for subtraction, 'div' for division and 'times' for multiplication: \n")


try:
    
    first_number = float(input("enter the first number: \n"))
    second_number = float(input("enter the second number: \n"))
    
    if operator == "add":
        print("you choose addition")
        print(first_number + second_number)
    elif operator == "sub":
        print(first_number - second_number)
    elif operator == "div":
        if first_number != 0:
            print(first_number / second_number)
        else:
            print("cannot divide by zero")
    elif operator == "times":
        print(first_number * second_number)
    else:
        print(f"{operator} is not valid, please enter a valid operator")
except:
    ValueError("Enter a number")
    
    