'''
Patel, Jenisha 760284
2024-01-08
U6C1 Calculator 
'''

def calculate(exp: str) -> float:
    i = 0

    if exp[i] == '-':
        i += 1

    while i < len(exp):
        if exp[i] in ['+', '-', '*', '/', '^']:
            break
        i += 1

    operand1 = float(exp[:i])
    operator = exp[i]
    operand2 = float(exp[i + 1:])

    #print(operand1)
    #print(operand2)
    #print(operator)
    
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    elif operator == '^':
        result = operand1 ** operand2

    return round(result, 3)