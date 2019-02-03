import threading
def pa(p):
    print("a: {}".format(p))
def pb(p):
    print("b: {}".format(p))
    a = input()
    print(a)
if __name__ == "__main__":
    t1 = threading.Thread(target=pa(65))
    t2 = threading.Thread(target=pb(65))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")