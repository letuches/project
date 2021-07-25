# task 3
num = int(input('номер месяца: '))
wi, sp, su, au = 'winter', 'spring', 'summer', 'autumn'
m = {12: wi, 1: wi, 2: wi, 3: sp, 4: sp, 5: sp, 6: su, 7: su, 8: su, 9: au, 10: au, 11: au, 0: 'неверный ввод'}

print(m[num])

season = [None, wi, wi, sp, sp, sp, su, su, su, au, au, au, wi]

print(season[num])

