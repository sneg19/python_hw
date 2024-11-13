# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# from random import randint
# n_list = list(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_list)
# m_list = list(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_list)
# s_list = sorted(n_list.intersection(m_list))
# print(s_list)

# from random import randint
# n_list = list(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_list)
# n_list = n_set = set
# m_list = list(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_list)
# m_list = m_set = set
# s_set = sorted(n_set.intersection(m_set))
# print(s_set)

# n_list = [1, 32, 23, 32, 45, 17]
# m_list = [2, 32, 56, 45, 32, 17]

n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

# n_list = list()
# m_list = list()

res =[]

for i in n_list:
    for j in m_list:
        if i == j:
            res.append(i)

res = set(res) 
sorted_res = sorted(res)


print(sorted_res)