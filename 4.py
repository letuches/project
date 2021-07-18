#4 задание
z = int(input("Введите целое положительное число: "))
y = 0
while z > 10:
    x = z % 10
    z = z // 10
    if x > y:
        y = x
if z > y:
    print(z)
else:
    print(y)




