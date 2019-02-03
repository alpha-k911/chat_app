import threading
import os
def task1():
    print("Task1 is assigned to thread: {}".format(threading.current_thread().name))
    print("Id of current thread is: {}".format(os.getpid()))

def task2():
    print("Task2 is assigned to thread: {}".format(threading.current_thread().name))
    print("Id of current thread is: {}".format(os.getpid()))

if __name__ == "__main__":
    print("Id of main program is: {}".format(os.getpid()))
    print("Name of Main program is: {}".format(threading.main_thread().name))

    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done")

