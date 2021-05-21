import threading
import time
import random
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)


class elemento():
    cantidad = 0

    def __init__(self, elemento):
        self.producto = elemento

    def nuevaCantidad(self, cantidad):
        self.cantidad = cantidad


def proceso(l1, l2, id):
    while True:
        while not (l1.locked() or l2.locked()):
            l1.acquire()
            try:
                elemento1.nuevaCantidad(random.randint(1, 100))
                logging.info(f'proceso {id} solicita {elemento1.cantidad} unidades de {elemento1.producto}')
                time.sleep(2)
                try:
                    l2.acquire()
                    elemento2.nuevaCantidad(random.randint(1, 10))
                    logging.info(f'proceso {id} solicita {elemento2.cantidad} unidades de {elemento2.producto}')
                    time.sleep(1)
                finally:
                    l2.release()
            finally:
                l1.release()
            time.sleep(1)


elemento1 = elemento("Tuercas")
elemento2 = elemento("Pernos")


def main():
    lockP = threading.Lock()
    lockT = threading.Lock()

    stock1 = threading.Thread(target=proceso, args=(lockP, lockT, 1))
    stock2 = threading.Thread(target=proceso, args=(lockT, lockP, 2))

    stock1.start()
    stock2.start()

    stock1.join()
    stock2.join()


if __name__ == '__main__':
    main()
