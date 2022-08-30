numb_n = int(input('Введи N : '))
j = 0
for i in range(2, numb_n):
    if i % 2 == 0:
        print(i, end=' ')
        j += 1
        if j % 5 ==0:
            print('\n')

# **Вывести четные числа от 2 до N по 5 в строку