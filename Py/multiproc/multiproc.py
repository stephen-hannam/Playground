from multiprocessing import Process, Manager
from time import sleep

def proc_0(msg, uid0, uid1):
    print("{0} from {1} {2}".format(msg, uid0, uid1))

def proc_1(msg,j):
    procs = []
    for i in range(10):
        procs.append(Process(target=proc_0, args=(msg,i,j,)))
    for proc in procs:
        proc.start()
    print("{0} sleeping".format(j))
    sleep(4)
    print("{0} woke".format(j))
    for proc in procs:
        proc.join()

def proc_2(msg):
    procs = []
    for j in range(10):
        procs.append(Process(target=proc_1, args=(msg,j,)))
    for proc in procs:
        proc.start()
    print("top sleeping")
    sleep(10)
    print("top woke")
    for proc in procs:
        proc.join()

if __name__=="__main__":
    proc_2("greetings")
