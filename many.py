# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# import random
# n = int(input('Введите количество элементов первого массива: '))
# list_1 = [random.randint(0, 100) for i in range(n)]
# print(list_1)

# # m = int(input('Введите количество эдементов второго массива: '))
# list_2 = [random.randint(0, 100) for i in range(n)]
# print(list_2)

# # res = list()

# for i in range(len(list_1)):
#     for j in range(len(list_2)):
#         if list_1[i] == list_2[j]:
#             # res[i] = list_1[i]
#             res = 

# print(res)


from random import randint
n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n_set)
m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(s_set)