1
def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))

2


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Mitkina', name='Lyubov', year='1985', city='Yekaterinburg', email='8697715@gmail.ru',
              telephone='8-922-18-63-216'))

3


def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')


4
1 вариант

def power(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))

2 вариант

def my_func():
    x = float(input("Введите положительное число, возводимое в степень: "))
    y = float(input("Введите степень ввиде целого отрацельного числа: "))
    res = x ** y
    return res
print(f'Рузультат - {my_func()}')



5
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')

my_sum()

6

def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()







