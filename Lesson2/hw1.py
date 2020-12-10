operand = None
operator = ''
res = 0

while True:
    try:
        operand = input('Input operand:')
        if operand == '=':
            break
        operand = int(operand)   

        operator = input('Input operator:')
        if operator == '=':
            break
        
        if operator == '+':
            res = res + float(operand)
        elif operator == '-':
            res = res - float(operand)
        elif operator == '*':
            res = res * float(operand)
        elif operator == '/':
            res = res / float(operand)
        else:
            print(f"Error, {operator} is not an operator")      

    except ValueError:
        print(f"Operand {operand} is not a number")


    except ZeroDivisionError:
        print("Вivide by zero is prohibited")
    

print(res)

