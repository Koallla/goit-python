operand = None
operator = ''
res = 0

while True:
    try:
        operator = input('Input operator:')
        if operator not in ['+', '-', '*', '/', '=']:
            print(f'Error, {operator} is not an operator')
            continue
        if operator == '=':
            break

        
        while True:
            try:
                operand = input('Input operand:')
                if operand == '=':
                    break
                operand = int(operand)
            except ValueError:
                print(f'Error, {operator} is not an operator')
                continue
            break

        if operand == '=':
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
