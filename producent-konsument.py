from multiprocessing import Queue, Process
import random
import time

def producent(kolejka):
  for i in range(30):
    numer = random.randint(1, 20)
    kolejka.put(numer)
    print(f"Producent {numer}")
    time.sleep(random.random())

def konsument(kolejka):
  for i in range(30):
    numer = kolejka.get()
    print(f"Konsument {numer}")
    time.sleep(random.random())

if __name__ == '__main__':
  kolejka = Queue()

  procesProducenta = Process(target=producent, args=(kolejka,))
  procesKonsumenta = Process(target=konsument, args=(kolejka,))

  procesProducenta.start()
  procesKonsumenta.start()

  procesProducenta.join()
  procesKonsumenta.join()