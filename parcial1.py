import threading
import time
import random
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

dato = 43
leido = False

semaphore = threading.Semaphore(1)


class Procesador(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global dato, leido
        while True:
            if not leido:
                logging.info(f'Se proceso el dato : {dato}')
                leido = True
                semaphore.release()
            time.sleep(random.randint(1, 5))


class Generador(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global dato, leido
        while True:
            semaphore.acquire()
            dato = random.randint(0, 100)
            logging.info(f'Se generó un nuevo dato = {dato}')
            leido = False


def main():
    hilos = []
    Generador().start()
    for _ in range(4):
        hilos.append(Procesador())

    for h in hilos:
        h.start()

    for thr in hilos:
        thr.join()


if __name__ == '__main__':
    main()
