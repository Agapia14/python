# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
#
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
import random


def bubble_sort(lst):
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break

        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
bubble_sort(array)
print('После сортировки:', array, sep='\n')

2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
array = [random.uniform(0, 50) for i in range(SIZE)]
print(array)


def merge_sort(a):
    if len(a) < 2:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:len(a)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1
    return a


print(merge_sort(array))

3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random
import cProfile


def median_search(lst, first, last):

    lst = lst.copy()
    ind = len(lst) // 2

    if first >= last:
        return lst[ind]

    pillar = lst[ind]
    i = first
    j = last

    while i <= j:

        while lst[i] < pillar:
            i += 1

        while lst[j] > pillar:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if ind < i:
        lst[ind] = median_search(lst, first, j)

    elif j < ind:
        lst[ind] = median_search(lst, i, last)

    return lst[ind]


def merge_sort(arr):

    def merge(fst, snd):
        res = []
        i, j = 0, 0

        while i < len(fst) and j < len(snd):

            if fst[i] < snd[j]:
                res.append(fst[i])
                i += 1

            else:
                res.append(snd[j])
                j += 1

        res.extend(fst[i:] if i < len(fst) else snd[j:])

        return res

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)


MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

# cProfile.run('median_search(array, 0, len(array) - 1)')

print(f'Сгенерирован массив из 2*{m}+1 = {size}  элементов:', array, sep='\n')

median = median_search(array, 0, len(array) - 1)
print(f'Медиана: {median}')
# print(array, '\n')

print('Отсортированный массив: ', merge_sort(array), sep='\n')
if median == merge_sort(array)[len(array)//2]:
    print('\nВерно')
else:
    print('\nОшибка!!!')
