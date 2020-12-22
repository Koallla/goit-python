operand = None
operator = ''
res = 0

while True:
    try:
        while True:
            try:
                operand = input('Input operand or symbol =:')
                if operand == '=':
                    break
                operand = int(operand)
            except ValueError:
                print(f'Error, {operator} is not an operator. Enter number or =')
                continue
            break

        if operand == '=':
            break
        


        while True:
            operator = input('Input operator:')
            if operator not in ['+', '-', '*', '/']:
                print(f'Error, {operator} is not an operator, please enter +, -, *, /')
                continue
            break

    
        if operator == '+':
            res += operand
        elif operator == '-':
            res -= operand
        elif operator == '*':
            res *= operand
        elif operator == '/':
            res /= operand
   
    
    except ZeroDivisionError:
        print('Вivide by zero is prohibited')
    

print(res)
