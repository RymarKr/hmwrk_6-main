# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """
    pass

#import random
#n = int(input('n = '))
#array = [random.randrange(0, 30) for i in range(n+1)]
array = [int(i) for i in input('Введите элементы массива: ').split()]
print(array)
min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))


for i in range(len(array)):
    if array[i]>=min and array[i]<=max:
        print(i, end=' ')