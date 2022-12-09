#Задача№5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.*
# Пример:

#             - 2*x^5 + 4*x + 5 = 0 
#             - 5*x^2 + 2*x + 43 = 0
#             - Результат: 7*x^2 + 6*x + 48 = 0
### ВАЖНО!!!!!!!!!! КОД НЕ РАБОТАЕТ (91 СТРОКА) (ДОПИСАН ДО КОНЦА), ТРЕБУЕТ ОПТИМИЗАЦИИ И 
### ПОХОДУ ПОШЕЛ НЕ ТЕМ ПУТЕМ
with open('ur1.txt','r') as ur1:
    data1 = ur1.readline()

with open('ur2.txt','r') as ur2:
    data2 = ur2.readline()

#Формируем первый  и втророй список из членов до = и через +
left1 = data1[:data1.index('=')]
lst1 =  left1.split(" + ")
# print(lst1)
left2 = data2[:data2.index('=')]
lst2 =  left2.split(" + ")
#print(lst2)


#Создаем списки для степеней и коэффициентов для 2х уравнений
#тут проверку на степен 1 и 0 для одного и другого уравнения
# для первого уравнения
eq_a1 = []
eq_n1 = []

for i in range(len(lst1)):
    if '^' not in lst1[i] and not lst1[i].isdigit():
        b1 = str(lst1[i][:-1])    
       
    elif str(lst1[i]).isdigit(): 
        c1 = lst1[i]

    if '^' in lst1[i] and 'x' in lst1[i]:
        n1 = lst1[i][(lst1[i].index('^') + 1):]
        a1 = lst1[i][:lst1[i].index('x')]
        eq_n1.append(n1)
        eq_a1.append(a1)
eq_n1.append(-1) # по -1 далее создаем флаг
# print(eq_n1)
# print(eq_a1)
# print(b1)
# print(c1)

eq_a2 = []
eq_n2 = []

for i in range(len(lst2)):
    if '^' not in lst2[i] and not lst2[i].isdigit():
        b2 = str(lst2[i][:-1])    
        print(b2)
    elif str(lst2[i]).isdigit(): 
        c2= lst2[i]
        print(c2)

    if '^' in lst2[i] and 'x' in lst2[i]:
        n2 = lst2[i][(lst2[i].index('^') + 1):]
        a2 = lst2[i][:lst2[i].index('x')]
        eq_n2.append(n2)
        eq_a2.append(a2)
eq_n2.append(-1) # по -1 далее создаем флаг
# print(eq_n2)
# print(eq_a2)
# print(b2)
# print(c2)


#Заполняю список общих стпеней от большей к меньшей для двух уравнений
#а также общий список аргументов с учетом полученной общей (или нет) степени

un_eq_n = []
un_eq_a = [] 

i = 0 
j = 0

for k in range(len(eq_n1) + len(eq_n2)-1): # если ни одна из степеней не совпадет
    if int(eq_n1[i]) > int(eq_n2[j]):
       un_eq_n.append(eq_n1[i])
       un_eq_a.append(eq_a1[i])
       if i < (len(eq_n1)-1):
            i+=1    
    elif int(eq_n1[i]) == int(eq_n2[j]):
        un_eq_n.append(eq_n1[i]) 
        un_eq_a.append(eq_a1[i] + eq_a2[i])
        if eq_n1[i] == -1 and eq_n2[j] == -1:#используем флаг для прерывания заполнения 
            break                            #общего списка степеней
        if i < (len(eq_n1)-1):
           i+=1
        if j < (len(eq_n2)-1):
            j+=1 
    elif int(eq_n1[i]) < int(eq_n2[j]):           
        un_eq_n.append(eq_n2[j])
        un_eq_a.append(eq_a2[i])
        if j < (len(eq_n2)-1):
            j+=1
un_eq_n.pop(-1)

bb = ''.join(map(str,b1 + b2))
cc = ''.join(map(str,c1 + c2))
b = ''.join(map(str,bb + 'x'))
c = ''.join(map(str,cc + 'x'))

res_str_0 = []                     # без коэффициентов b и с 
for e in range(len(un_eq_n)):
    res_str_0.append(un_eq_a[i],'x^',un_eq_n[i])

res_str = ''.join(map(str,res_str_0 + b + c))
print(res_str)

    



    



