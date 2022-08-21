name : str = input('Введи имя : ')
age : str = input('Введи возраст : ')
city : str = input('Введи город : ')
line_f = f'Привет {name}, твой возраст {age}, ты из города {city}'
line_concat = 'Привет ' + name + ', твой возраст ' + age + ', ты из города ' + city
line_format = 'Привет {}, твой возраст {}, ты из города {}'.format(name, age, city)
print(line_f)
print(line_format)
print(line_concat)

