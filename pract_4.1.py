n = int(input('Введи степень : '))
step = [i for i in range(1, n+1)]
spis = [2**n for n in step]
print(spis)

#Заполнить список степенями числа 2 (от 2^1 до 2^n)