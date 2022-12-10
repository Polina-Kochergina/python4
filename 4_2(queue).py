         
import queue
import threading
import random as rd
from numpy import exp

# создаем экземпляры очереди (2 штуки для теста)
q = queue.Queue()
p = queue.Queue()

# класс, получающий из q элементы и выполняющий вычисления с ними

class Reciever:
    def  __init__(self, q):
        self.num = 0
        self.q = q

    def recieve(self):
        i = 1

        while True:

            x = self.q.get()

            match x:
                case "start":
                    self.num += 1
                case "finish":
                    self.num -= 1
                case _:
                    print(f"номер {i}:{exp(x)}")
                    i += 1


            if (self.num == 0):
                break

# класс генерирующий числа порциями n

class Sender:
    def __init__(self, n, q):
        self.n = n
        self.q = q
        self.q.put("start")

        self.list = []

    def __call__ (self):
        for i in range(self.n):
            self.list.append(rd.random())
            self.q.put(self.list[i])

        self.q.put("finish")


            


senders = []
# senders1 = []

for i in range(10):
    senders.append(Sender(2, p))


for i in senders:
    threading.Thread(target = i).start()

# for i in senders1:
    # threading.Thread(target = i).start()

r = Reciever(p)
# r1 = Reciever(q)

threading.Thread(target = r.recieve).start() 
# threading.Thread(target = r1.recieve).start() 

