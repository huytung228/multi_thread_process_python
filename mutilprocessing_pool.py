# Pool la co che tu phan chia nhiem vu ra cac core, co the hieu tuong tu nhu apache spark
import multiprocessing
import os

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n * n)
    
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    p = multiprocessing.Pool()
    print(p.map(square, my_list))