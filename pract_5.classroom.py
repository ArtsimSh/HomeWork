#stroka = input('слово : ')
#stroka = stroka.lower()
#palindrom = stroka[::-1]
#if stroka == palindrom:
#    print('Палиндром')
#else:
#    print(('Не палиндром'))

#вводится слово определить является ли оно палиндромом

# stroka = input('Строка : ')
# for _ in range(len(stroka)):
#     letter = stroka[_]
#     numb = stroka.count(letter)
#     if numb == 1:
#         print(letter)

# вводится строка, вывести уникальные символы строки ( те которые встречаются один раз)

# word_1: str = input('Введи первое слово : ')
# word_2: str = input('Введи вторе слово : ')
# if len(word_1) == len(word_2):
#     for _ in range(len(word_1)):
#         numb = word_1.count(word_2[_])
#         if numb != 1:
#             print('Не анограмма')
#             break
#         else:
#             print('Анограмма')
#             break

#вводятся два слова определить являются ли они анограммами (игра, рига)

# numb_n = int(input('Введи число : '))
# fact = 1
# for i in range(1, numb_n+1):
#     fact *= i
# print(fact)

#вводится числа посчитать его факториал

# numb_n = str(input('Введи число : '))
# while numb_n.isdigit():
#     break
# else:
#     print('Не угадал, попробуй ещё раз')

#пользователь вводит строку переспрашивать до тех пор пока пользователь не введёт число

# numb_n = int(input('Введи количество чисел N : '))
# sum = 0
# for _ in range(1, numb_n+1):
#     sum = sum + int(input(f"Введи число {_} "))
# sum = sum / numb_n
# print(sum)

#составить программу для вычисления среднего арифметического N произвольно вводимых числел

numb_n = int(input('Введи степень : '))
for n in range(1, numb_n):
    print(n)
    for k in range(1, n):
        if k == 1:
            print(k, end=' ')
        else:
            k = (n-1) + (k-1)
            print(k, end=' ')


#Написать программу генерации треугольника паскаля указанной глубины

