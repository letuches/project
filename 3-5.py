#  #  task 5

def sum_nums(num, term):
    lst = num.split(' ')
    sum_lst = 0
    for i in lst:
        if i == term:
            break
        sum_lst += int(i)
    return sum_lst


term = '#'
finished = False
values = 0
while not finished:
    num = input('Ввести числа разделенные пробелом: ')
    values += sum_nums(num, term)
    finished = term in num
    print(values)



