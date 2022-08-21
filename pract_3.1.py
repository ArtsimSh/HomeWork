text: str = input('Введи предложение : ')
#len_world = len(text)
text_split = text.split()
text_join = '--'.join(text_split)
print(text_join)
#print(text_split, sep='--')

