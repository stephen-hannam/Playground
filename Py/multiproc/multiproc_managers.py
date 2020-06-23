from multiprocessing import Process, Manager
from time import sleep

def proc_0(msg, uid0, uid1,man,L):
    ret = "{0} from {1} {2}".format(msg, uid0, uid1)
    ns = man.Namespace()
    setattr(ns, "result".format(uid0,uid1), ret)
    L.append(ns)

def proc_1(msg,j,man,L):
    procs = []
    for i in range(10):
        procs.append(Process(target=proc_0, args=(msg,i,j,man,L)))
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()

def proc_2(msg):
    manager = Manager()
    L = manager.list()
    procs = []
    for j in range(10):
        procs.append(Process(target=proc_1, args=(msg,j,manager,L)))
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()
    return L

if __name__=="__main__":
    L = proc_2("greetings")
    print(L)
