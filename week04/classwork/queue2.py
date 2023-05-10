import queue
import threading
import time

def read_thread(q: queue.Queue):
    
    while True:
        obj = q.get()
        
        print(f'GET: {obj}')
        time.sleep(0.1)
        
        if obj == None:
            break

def write_thread(q):
    for i in range(10):
        q.put(i)
        #time.sleep(0.2)
    
    q.put(None)

def main():
    q = queue.Queue()

    t1 = threading.Thread(target=read_thread, args=(q,))
    t2 = threading.Thread(target=write_thread, args=(q,))
    t3 = threading.Thread(target=write_thread, args=(q,))
    
    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    main()