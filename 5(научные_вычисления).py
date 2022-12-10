import numpy as np
import time
from random import randint
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

n=10



def listmul1(n):
    ''' element-wise multiplication function of one-dimensional arrays'''
    listmul = []
    list1 = [randint(0, 10) for i in range(0, n)]
    list2 = [randint(0, 10) for i in range(0, n)]
    for i in range(0,len(list1)):
        x = list1[i]*list2[i]
        listmul.append(x)



def listmul2(n):
    ''' element-wise multiplication function of two-dimensional arrays'''


    list1 = [randint(0, 10) for i in range(0, n)]
    list2 = [randint(0, 10) for i in range(0, n)]
    list3 = [randint(0, 10) for i in range(0, n)]
    list4 = [randint(0, 10) for i in range(0, n)]

    listdim2_1 = [list1, list2, list3, list4]
    listmul = []

    for i in range(0,len(listdim2_1)):
        for j in range(0,len(list1)):
            x = listdim2_1[i][j]*listdim2_1[i][j]
            listmul.append(x)



def listmul3(n):
    ''' element-wise multiplication function of three-dimensional arrays'''

    listmul = []

    list1 = [randint(0, 10) for i in range(0, n)]
    list2 = [randint(0, 10) for i in range(0, n)]
    list3 = [randint(0, 10) for i in range(0, n)]
    list4 = [randint(0, 10) for i in range(0, n)]

    listdim2_1 = [list1, list2, list3, list4, list1]

    listdim3_1 = [listdim2_1, listdim2_1]



    for i in range(0,len(listdim3_1)):
        for j in range(0,len(listdim2_1)):
            for k in range(0,len(list1)):
                x = listdim3_1[i][j][k]*listdim3_1[i][j][k]
                listmul.append(x)

# апроксимирующие функции 

def mapping1(values_x, a, b, c): 
    y = []
    for i in range(len(values_x)):
        y.append(a*values_x[i]**2 + b*values_x[i] + c)
    return y

def mapping2(values_x, a, b): 
    y = []
    for i in range(len(values_x)):
        y.append(a*values_x[i] + b)
    return y

time2 = []
time1 = []
time3 = []
num = []


print("start list")

for i in range(100,1000, 100):
    time_list1 = time.time()
    listmul1(i)
    time1.append(time.time()-time_list1)

for i in range(100,1000, 100):
    num.append(i)
    time_list1 = time.time()
    listmul2(i)
    time2.append(time.time()-time_list1)

for i in range(100,1000, 100):
    time_list1 = time.time()
    listmul3(i)
    time3.append(time.time()-time_list1)

print("finih list")


# ищем коэфф апроксимации для 3 наборов данных

args1, _ = curve_fit(mapping2, num, time1)
args2, _ = curve_fit(mapping2, num, time2)
args3, _ = curve_fit(mapping2, num, time3)

# х от 0 и до 1000
x = [x for x in range(0,1000, 10)]
# находим у
y1 = mapping2(x, args1[0], args1[1])
y2 = mapping2(x, args2[0], args2[1])
y3 = mapping2(x, args3[0], args3[1])

# теоретические у для num (кол-во тестируемых размеров)
y_1 = mapping2(num,  args1[0], args1[1])
y_2 = mapping2(num,  args2[0], args2[1])
y_3 = mapping2(num,  args3[0], args3[1])

# ошибки
err1 = [abs(time1[i] - y_1[i]) for i in range(len(time1))]
err2 = [abs(time2[i] - y_2[i]) for i in range(len(time1))]
err3 = [abs(time3[i] - y_3[i]) for i in range(len(time1))]



# класс массивов, у которых одна из размерностей задается = n , остальные фиксированные
# (подгон под списки, чтобы совпадали по кол-ву эл-ов)

class matrix_size_n(object):
    def __init__(self, n):
        
        self.matrix1 = np.fromiter(range(n), dtype='int32')
        self.matrix2 = np.fromiter(range(n*5), dtype='int32')
        self.matrix3 = np.fromiter(range(n*5*2), dtype='int32')

        self.matrix2.resize(n, 5)
        self.matrix3.resize(n, 5, 2)
        

# создаем экземпляры класса 10шт разного размера (100, 200, ..., 1000)

M = []
for i in range(100, 1000, 100):
    M.append(matrix_size_n(i))

print("start array")

# for до 100000, так как multiply оч быстрый и время гораздо меньше 1 с 

mtrx_time1 = []
for i in range(len(M)):
    t = time.time()
    for _ in range(1, 100000):
        np.multiply(M[i].matrix1, M[i].matrix1)
    mtrx_time1.append((time.time()-t)/100000)


mtrx_time2 = []
for i in range(len(M)):
    t = time.time()
    for _ in range(1, 10000):
        np.multiply(M[i].matrix2, M[i].matrix2)
    mtrx_time2.append((time.time()-t)/10000)
   



mtrx_time3 = []
for i in range(len(M)):
    t = time.time()
    for _ in range(1, 10000):
        np.multiply(M[i].matrix3, M[i].matrix3)
    mtrx_time3.append((time.time()-t)/10000)

print("finish list")



print(mtrx_time3)

# ищем коэфф апроксимации для 3 наборов данных

npargs1, _ = curve_fit(mapping2, num, mtrx_time1)
npargs2, _ = curve_fit(mapping2, num, mtrx_time2)
npargs3, _ = curve_fit(mapping2, num, mtrx_time3)


np_y1 = mapping2(x, npargs1[0], npargs1[1])
np_y2 = mapping2(x, npargs2[0], npargs2[1])
np_y3 = mapping2(x, npargs3[0], npargs3[1])

npy_1 = mapping2(num,  npargs1[0], npargs1[1])
npy_2 = mapping2(num,  npargs2[0], npargs2[1])
npy_3 = mapping2(num,  npargs3[0], npargs3[1])

nperr1 = [abs(mtrx_time1[i] - npy_1[i]) for i in range(len(npy_1))]
nperr2 = [abs(mtrx_time2[i] - npy_2[i]) for i in range(len(npy_1))]
nperr3 = [abs(mtrx_time3[i] - npy_3[i]) for i in range(len(npy_1))]


# строим 2 графика с легендой и ошибками

fig, axes = plt.subplots(2, figsize=(8.5, 8))

axes[0].plot(x, y1, color = "crimson", linewidth = 1.3, label = 'dim = 1')
axes[0].plot(x, y2, color = "green", linewidth = 1.3,  label = 'dim = 2')
axes[0].plot(x, y3, color = "orange", linewidth = 1.3,  label = 'dim = 3')
axes[0].errorbar(num, y_1, yerr=err1, linestyle='none', ecolor='firebrick', elinewidth=1, capsize=2, capthick=2)
axes[0].errorbar(num, y_2, yerr=err2, linestyle='none', ecolor='seagreen', elinewidth=0.8, capsize=2, capthick=2)
axes[0].errorbar(num, y_3, yerr=err3,linestyle='none', ecolor='gold', elinewidth=0.8, capsize=2, capthick=2)
axes[0].legend()

axes[1].plot(x, np_y1, color = "crimson", linewidth = 1.3, label = 'dim = 1')
axes[1].plot(x, np_y2, color = "green", linewidth = 1.3,  label = 'dim = 2')
axes[1].plot(x, np_y3, color = "orange", linewidth = 1.3,  label = 'dim = 3')
axes[1].errorbar(num, npy_1, yerr=nperr1, linestyle='none', ecolor='firebrick', elinewidth=0.8, capsize=1, capthick=1)
axes[1].errorbar(num, npy_2, yerr=nperr2, linestyle='none', ecolor='seagreen', elinewidth=0.8, capsize=1, capthick=1)
axes[1].errorbar(num, npy_3, yerr=nperr3, linestyle='none', ecolor='darkorange', elinewidth=0.8, capsize=1, capthick=1)

plt.show()
