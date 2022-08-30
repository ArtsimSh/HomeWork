numb_n = int(input('Введи колличество N первых чисел = '))
numb_m = int(input('Введи M кратное = '))
numb_k = int(input('Введи число больше K = '))
numbers = []
while len(numbers) != numb_n:
    if numb_k % numb_m == 0:
        numbers.append(numb_k)
    numb_k += 1
print(numbers)

#Вывести первые N цисел кратные M и больше K