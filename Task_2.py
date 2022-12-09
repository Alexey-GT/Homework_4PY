#Два числа нужно НОК и НОД
import math
def find_mult(num):
    div = 2
    multiplier = []
    while num > div:
        while num % div == 0:
            multiplier.append(div)
            num//=div #чтобы не было зацикливания
            div+=1
    return multiplier
a, b = 18, 48
multiplier_a = find_mult(a)
multiplier_b = find_mult(b)
res =  1 
for i in set(multiplier_b).intersection(set(multiplier_a)):
    res*=i
print('НОД: ',res)
print(a*b/res)#НОК