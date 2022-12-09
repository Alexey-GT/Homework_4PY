#Задача№4
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать
#  в файл многочлен степени k(до 6 степени).*

#         *Пример:* 

#         - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите число '))
lst = []

while k >= 0:
    m = randint(0,100)

    ch_0 = [m,'x^',k]
    sch = ''.join(map(str,ch_0))
    lst.append(sch)
    str_0 = " + ".join(map(str,lst))
       
    print(str_0)

    if k == 1:
        ch_1 = [' + ',m,'x']
        #print([m,"x"]) 
        str_1 = "".join(map(str,ch_1))
       
        print(str_1)
    
    if k == 0:
        ch_2 = [' + ',m,' = 0']
        str_2 = ''.join(map(str,ch_2))
        print(str_2)
    k-=1
equation_str = str_0 + str_1 + str_2

print(equation_str) 
data = open('polynomial.txt','a')
data.writelines(equation_str)
data.close()
