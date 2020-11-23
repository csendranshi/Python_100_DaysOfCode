def add(n1,n2):
    return(n1+n2)

def sub(n1,n2):
    return(n1-n2)

def divide(n1,n2):
    return(n1/n2)

def multiply(n1,n2):
    return(n1*n2)

operations={
    '+':add,
    '-':sub,
    '/':divide,
    '*':multiply
}

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

for symbol in operations:
    print(symbol)
op_symbol = input("Pick an operation from the above lines: ")

calculation_function = operations[op_symbol]
first_answer = calculation_function(n1,n2)
print(f"{n1} {op_symbol} {n2} = {first_answer}")

op_symbol = input("Pick an operation from the above lines: ")
n3 = int(input("Whats the next number: "))
calculation_function = operations[op_symbol]
second_answer = calculation_function(first_answer,n3)
print(f"{first_answer} {op_symbol} {n3} = {second_answer}")