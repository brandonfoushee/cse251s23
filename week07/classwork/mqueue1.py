import multiprocessing
import queue
import time

AMOUNT = 10


def sender(q, data, count):
    for i in range(count):
        data[i] = i
        q.put(data[i])
    q.put(None)

    time.sleep(3)
    print(f'sender: {data[0]}')


def receiver(q, data):
    while True:
        item = q.get()
        if item == None:
            break
        print(f'{item=}')
    data[0] = 100
    print(f'receiver: {data[0]}')

def main():
    q_threading = queue.Queue()
    q = multiprocessing.Queue()

    normal_list = [0] * AMOUNT
    print(f'{type(normal_list)}')

    data = multiprocessing.Manager().list([0] * AMOUNT)
    p1 = multiprocessing.Process(target=sender, args=(q, data, AMOUNT))
    p2 = multiprocessing.Process(target=receiver, args=(q, data))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
