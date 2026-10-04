def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

try:
    operation=input("What will you be needing to work out today(add,minus,divide,multiply): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "add":
        print(add(num1, num2))
    elif operation == "minus":
        print(minus(num1, num2))
    elif operation == "multiply":
        print(multiply(num1, num2))
    elif operation == "divide":
        print(divide(num1, num2))

except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Maths Error.")