numb = int(input('ВВеди кол-во человек : '))
dict_end = {i: {'name': input('Введи имя : '), 'email': input('Введи email :')} for i in range(1, numb+1)}
print(dict_end)
