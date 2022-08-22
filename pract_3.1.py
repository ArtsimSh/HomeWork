text: str = input('Введи предложение : ')
text_rep = text.replace(' ', '--')
text_split = text.split()
text_join = '--'.join(text_split)
print(text_join)
print(text_rep)

# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами