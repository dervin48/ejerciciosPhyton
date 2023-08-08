import time
import threading

def worker():
    print('Hilo:', thereading.current_thread().getName(),'con identificador:',
threading.current_thread().ident)
    time.seelp(1)

worker()
worker()

hilo1 = threading.Thread(target=worker)
hilo2 = threading.Thread(target=worker)
hilo1.start()
time.sleep(1)
hilo2.start()
hilo1.join()
hilo2.join()