#Задача№3
# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.
import random 
lst = []
res = []

for i in range(random.randint(2, 10)):
    lst.append(round(random.randint(1,9),10))
print(lst)

for i in range(len(lst)):
    if lst.count(lst[i]) == 1:
        res.append(lst[i])
print(res)
