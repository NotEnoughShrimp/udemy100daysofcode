# Calculator follow udemy's course
import calculatorart

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(calculatorart.logo)
    num1 = float(input("enter first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operator = input("please select an operation: ")
        num2 = float(input("enter second number: "))

        calculation = operations[operator]
        answer = calculation(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")
        if input(f"Type 'y' to consinue calculating with {answer} or 'n' for new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()
