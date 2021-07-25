# task 3-6

def int_func(text):
    word = text[0].upper() + text[1:].lower()
    return word


print(int_func('proba'))

words = input('Enter some words: ')
for word in words.split(' '):
    print(f'{int_func(word)}', end=' ')
