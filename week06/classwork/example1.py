import multiprocessing
import time

count = 0

class MyProcess(multiprocessing.Process):
    def __init__(self, index):
        multiprocessing.Process.__init__(self)
        self.index = index
    
    def run(self):
        global count
        count += 1
        print(f'{self.index=}: {self.pid=}, {count=}')

def myfunc(index):
    print(f'{multiprocessing.current_process()}: {index=}')

def main():
    print(f"{multiprocessing.current_process().pid}")

    processes = []
    for i in range(5):
        #p = MyProcess(i)
        p = multiprocessing.Process(target=myfunc, args=(i,))
        p.start()
        time.sleep(0.001)
        processes.append(p)
    
    for p in processes:
        p.join()

#print(f"{__name__}")
if __name__ == '__main__':
    main()
