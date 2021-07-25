# task 2
l = list(input("Введите любые символы "))

for i in range(len(l) // 2):
    k1, k2 = 2 * i, 2 * i + 1
    l[k1], l[k2] = l[k2], l[k1]

print(l)
