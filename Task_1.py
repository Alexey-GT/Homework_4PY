#Задачa№1
# Вычислить число ПИ c заданной точностью d

#     *Пример:* 

#     - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10
import math
pi = math.pi
d = int(input('Введите точность: '))
#str = ''.join(map(str,s))
str = str(pi)
print(type(str))
print(str[:d+2])