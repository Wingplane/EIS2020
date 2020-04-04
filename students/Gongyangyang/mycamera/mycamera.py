import mcpi.minecraft as minecraft
import mcpi.block as block
from movedetect import *
from myhouse import *
import threading


threads = []

t1 = threading.Thread(target=Inwhichhouse) # 使用多线程，使得两个检测循环同时进行
threads.append(t1)
t2 = threading.Thread(target=movedetect)
threads.append(t2)
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print ("退出")