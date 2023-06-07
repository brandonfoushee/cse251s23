import multiprocessing
from multiprocessing.connection import PipeConnection
import time


def sender1(conn: PipeConnection):
    msgs = ["Hello, ", "how ", "are ", "you?"]

    for msg in msgs:
        conn.send(msg)

    time.sleep(3)
    conn.send(None)


def sender2(conn: PipeConnection, recv: PipeConnection):

    while True:
        msg = recv.recv()
        conn.send(msg)
        if msg == None:
            break

        #print(f'1: {msg=}')


def receiver(recv: PipeConnection):

    while True:
        msg = recv.recv()
        if msg == None:
            break
        print(f'{msg=}')


def main():
    send_conn1, recv_conn1 = multiprocessing.Pipe()
    send_conn2, recv_conn2 = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=sender1, args=(send_conn1,))
    p2 = multiprocessing.Process(target=sender2, args=(send_conn2, recv_conn1))
    p3 = multiprocessing.Process(target=receiver, args=(recv_conn2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == "__main__":
    main()
