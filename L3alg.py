1
найти количество кратных чисел Python
a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1

2
четные индексы python
from random import randint
N = 5
arr = [0] * N
even = []
for i in range(N):
    arr[i] = randint(10, 19)
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных элементов: ', even)

3
поменять местами элементы массива
from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

# 1-й вариант
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn + 1, mn, imx + 1, mx))
arr[imn], arr[imx] = arr[imx], arr[imn]

# 2-й вариант (классический)
# ~ mn = 0
# ~ mx = 0
# ~ for i in range(N):
# ~ if arr[i] < arr[mn]:
# ~ mn = i
# ~ elif arr[i] > arr[mx]:
# ~ mx = i
# ~ print('arr[%d]=%d arr[%d]=%d' % (mn+1, arr[mn], mx+1, arr[mx]))
# ~ b = arr[mn]
# ~ arr[mn] = arr[mx]
# ~ arr[mx] = b

for i in range(15):
    print(arr[i], end=' ')
print()

4
найти самый часто встречающийся элемент из массива python
from random import random

N = 15
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')

5
максимальное отрицательное число python (питон)

from random import random

N = 15
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])

6
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать
from random import random
N = 10
a = [0]*N
for i in range(N):
    a[i] = int(random()*50)
    print('%3d' % a[i], end='')
print()
min_id = 0
max_id = 0
for i in range(1,N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])
if min_id > max_id:
    min_id, max_id = max_id, min_id
summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print(summa)

7
найти два минимальных элемента массива python
from random import random

N = 10
a = []
for i in range(N):
    a.append(int(random() * 100))
    print("%3d" % a[i], end='')
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print("№%3d:%3d" % (min1 + 1, a[min1]))
print("№%3d:%3d" % (min2 + 1, a[min2]))

8
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу

M = 5
N = 4
a = []
for i in range(N):
    b = []
    s = 0
    print("%d-я строка:" % i)
    for j in range(M - 1):
        n = int(input())
        s += n
        b.append(n)
    b.append(s)
    a.append(b)

for i in a:
    print(i)

9

Найти максимальный элемент среди минимальных элементов столбцов матрицы
from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
