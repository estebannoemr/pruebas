from src.operations import add, substract, multiply, divide
#from src.operations import *

def calculate(a, b, operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return substract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        raise ValueError(f"Invalid operator: {operator}")

