# task 1

f_val = float(input("Первое число: "))
s_val = float(input("Второе число: "))
if s_val == 0:
   print("Ошибка ввода, деление на 0 невозможно!!!")
else:
    def func(f_val, s_val):
        return f_val / s_val
    print(func(f_val, s_val))

