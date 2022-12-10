# import threading
import time
from multiprocessing import Pool
from matplotlib import pyplot as plt 

t = time.time()


def func(x):
    for i in range(1, 10000):
        for j in range(1, 100):
            m = x*i*j


if __name__ == '__main__':
    timer = []
    arg = [5]

    for ker in range(1, 10):
        t0 = time.time()
        p = Pool(ker)
        for i in range(5**2):
            pol = p.map(func, arg)

        timer.append((time.time()-t0))
        print(ker)

   
    print(timer.index(min(timer))+1)

    print(f'{time.time() - t} time')
    x = range(1, 10)
    plt.plot(x, timer)
    plt.show()