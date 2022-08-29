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


word_1: str = input('Введи первое слово : ')
word_2: str = input('Введи вторе слово : ')
if len(word_1) == len(word_2):
    for _ in range(len(word_1)):
        numb = word_1.count(word_2[_])
        if numb != 1:
            print('Не анограмма')
            break
        else:
            print('Анограмма')
            break

#вводятся два слова определить являются ли они анограммами (игра, рига)