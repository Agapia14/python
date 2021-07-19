'''1. Написать программу, которая будет складывать, вычитать, умножать или
делить два числа. Числа и знак операции вводятся пользователем. После
выполнения вычисления программа не должна завершаться, а должна запрашивать
новые данные для вычислений. Завершение программы должно выполняться при вводе
символа '0' в качестве знака операции. Если пользователь вводит неверный знак
(не "0", "+", "-", "*", "/"), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции. Также сообщать пользователю о невозможности
деления на ноль, если он ввел 0 в качестве делителя.'''

while True:
    try:
        number1, operation, number2 = [
                i for i in
                input(
                    'Введите математическое выражение (число операнд число): '
                    ).split()
                ]
    except ValueError:
        print('Неправильный ввод.')
        continue
    number1 = int(number1)
    number2 = int(number2)

    if operation == '0':
        break
    elif operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')

2
# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


nums = input('Введите многозначное число\n')
even = []
odd = []
for i in nums:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f'В введенном числе {len(even)} четных числа {even} и {len(odd)} нечетных {odd}')

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


inp = input('Введите многозначное число\n')
print(f'Отзеркаленое число {inp[::-1]}')

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите кол-во итераций\n'))
type = int(input('Выберите вариант выполнения\n'
                 '1 - С помощью цикла\n'
                 '2 - С помощью рекурсивной функции\n'))
if type == 1:  # Вариант 1(Цикл):
    num = 1
    i = 0
    while i != n:
        num = num / (-2)
        i += 1
    print(f'Результат после {n} итераций равен {num} (Цикл)')
elif type == 2:  # Вариант 2(рекурсивный): Считаю его для данной задачи излишним
    def rec4(i, num, n):
        if i == n:
            return num
        elif i <= n:
            return rec4(i + 1, num / (-2), n)


    print(rec4(0, 1, n))

    # 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
    # Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


from beautifultable import BeautifulTable

table = BeautifulTable()

for c in (chr(i) for i in range(32, 127)):
    table.append_row([ord(c), c])
print(table)

# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

randnum = random.randint(0, 11)


def forecaster(randnum, t):
    answer = int(input('Введите число\n'))
    if randnum == answer:
        print(f'Верно! Вы угадали число!')
    elif answer != randnum:
        print(f'Неверно, попробуйте еще раз, увас осталось {t - 1} попыток.')
        return forecaster(randnum, t - 1)


forecaster(randnum, 10)

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

operand = input('Введите многозначное число\n')
operator = input('Введите цифку которую нужно найти во введенном числе\n')
count = 0
for i in operand:
    if i == operator:
        count += 1
    else:
        pass

print(f'В числе {operand} цтфра {operator} встречается {count} раз')

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

a = (input('Введите число A\n'))
a1 = sum(map(int, str(a)))
b = (input('Введите число B\n'))
b1 = sum(map(int, str(b)))
c = (input('Введите число C\n'))
c1 = sum(map(int, str(c)))

if a1 > b1 and a1 > c1:
    print(f'Наибольшее по сумме цифр число A({a}). Сумма цифр = {a1}')
elif b1 > a1 and b1 > c1:
    print(f'Наибольшее по сумме цифр число B({b}). Сумма цифр = {b1}')
else:
    print(f'Наибольшее по сумме цифр число C({c}). Сумма цифр = {c1}')
