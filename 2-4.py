# task 4

a = input("Ввод строки: ")
b = a.split(' ')

for num, word in enumerate(b):
    print(f'{num} - {word[:10]}')
