from art import logo

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

def calulator():
    print(logo)
    n1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)

    run = True
    while run:
        op_symbol = input("Pick an operation: ")
        n2 = float(input("Enter the next number: "))
        calculation_function = operations[op_symbol]
        first_answer = calculation_function(n1,n2)
        print(f"{n1} {op_symbol} {n2} = {first_answer}")

        rerun = input(f"Type 'y to continue with {first_answer}, or type 'n to exit: ")
        if rerun == 'n':
            run = False
            calulator()
        else:
            n1 = first_answer

calulator()