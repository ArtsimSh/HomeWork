numb_n = int(input('Введи колличество N первых чисел = '))
numb_m = int(input('Введи M кратное = '))
numb_k = int(input('Введи число больше K = '))
numbers = [i for i in range(1, 100) if i % numb_m == 0 and i > numb_k]
print(numbers[0:numb_n])

#Вывести первые N цисел кратные M и больше K