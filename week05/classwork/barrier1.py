import threading
import time
import random

def test_with_barrier(synchronizer: threading.Barrier):
    
    print(f'{threading.current_thread().name}: BEFORE SLEEP\n', end="")
    time.sleep(random.uniform(0.5, 2.0))
    print(f'{threading.current_thread().name}: AFTER SLEEP\n', end="")
    
    synchronizer.wait()
    now = time.time()
    
    print(f'{threading.current_thread().name}: The current time is {now}\n', end="")
 
if __name__ == '__main__':

    synchronizer = threading.Barrier(4)

    threads = []
    for _ in range(4):
        t = threading.Thread(target=test_with_barrier, args=(synchronizer,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
