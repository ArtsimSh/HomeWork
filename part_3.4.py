numb1 : float = float(input('Веди первое число : '))
numb2 : float = float(input('Веди второе число : '))
numb3 : float = float(input('Веди третье число : '))
plus : int = int(numb1>=1) + int(numb2>=1) + int(numb3>=1)
minus : int = int(numb1<=-1) + int(numb2<=-1) + int(numb3<=-1)
print(plus, minus)

#Пользователь вводит 3 числа, сказать сколько из них положительных
и сколько отрицательных