# Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
from random import random



d = float(input('Task #1 \nВведите точность знаков pi: '))
n = 0

while d %1 > 0: 
    n +=1
    d *= 10

print('Число знаков = ', n)
print(round(math.pi,n))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
d = int(input('\n Task #2 Список простых множителей \nВведите нат.число: '))
de = 2
res_del = []
while d > 1:
    if d % de == 0:
        d = d / de
        res_del.append(de)
        de = 2
    else:
        de += 1
print(res_del)

# # Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# #  элементов исходной последовательности.

list = [1,1,34,54,2,4,66,66,2,1,54,33,54,76,9,98,997,45,66,54]
exc_list = []
# exc_list = [i for i in list if not i in exc_list] не работает
for i in list:
    if not i in exc_list:
        exc_list.append(i)
print("\n Task #3 \nИсходный список: ", list)
print('Неповторяющийся список: ', exc_list)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('\n Task #4 Многочлен Х\nВведите степень Х (нат.число): '))
form = ''
a = randint(-100,100)
form += str(a)+'*X^'+str(k)
for i in range(k-1,1, -1): 
    a = randint(-100,100)
    if a > 0:
        form += ' + ' + str(a)+'*X^'+str(i)
    elif a < 0:
        form += ' - ' + str(-a)+'*X^'+str(i)
a= randint(-100,100)
if a > 0:
        form += ' + ' + str(a)+'*X'
elif a < 0:
        form += ' - ' + str(-a)+'*X'
a = randint(-100,100)
if a > 0 :
    form += ' + ' + str(a) + ' = 0'
elif a < 0:
    form += ' - ' + str(-a) + ' = 0'
print(form)
data = open('dataout.txt', 'w')
data.write(form)
data.close()

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
print('\nTask #5 Сумма многочленов')
s_1 = open('task5 sample1.txt', 'r')
      
s_2 = open('task5 sample2.txt', 'r')

lst1 = s_1.read() + s_2.read()
print('Сумма многочленов: ', lst1)        
newdata = open('rez_data.txt', 'w')
newdata.writelines(lst1)
s_1.close()
s_2.close()
newdata.close()
