numb_1 = float(input('Введи первое число : '))
calc = input('Введи действие : ')
numb_2 = float(input('Введи второе число : '))
if calc == '+':
    end_calc = numb_1 + numb_2
    print('Результат : ', end_calc)
elif calc == '-':
    end_calc = numb_1 - numb_2
    print('Результат : ', end_calc)
elif calc == '/':
    end_calc = numb_1 / numb_2
    print('Результат : ', end_calc)
elif calc == '*':
    end_calc = numb_1 * numb_2
    print('Результат : ', end_calc)
else:
    print('Неверная операция :')

# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число