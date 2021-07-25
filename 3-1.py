# task 1

val1 = float(input("Первое число: "))
val2 = float(input("Второе число: "))
if val2 == 0:

    print("Ошибка ввода, деление на 0 невозможно!!!")
else:
    def func(val1, val2):
        return val1 / val2


    print(func(val1, val2))
