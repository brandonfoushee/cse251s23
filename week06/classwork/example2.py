import multiprocessing
import time
import os

def square(n):
    n **= 2
    time.sleep(0.1)
    return n

if __name__ == '__main__':
    inputs = list(range(101))
    
    count = multiprocessing.cpu_count()
    
    print(f'{count=}')
    
    outputs = []
    with multiprocessing.Pool(15) as p:
        outputs = p.map(square, inputs)
    
    print(f'{outputs=}')