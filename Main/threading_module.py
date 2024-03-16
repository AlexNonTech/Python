import time
import threading


def calculate():
    time.sleep(3)
    print(True + True)


def message():
    time.sleep(4)
    print(f"Hello {__name__}")


def do_something():
    time.sleep(5)
    print("i was doing something...")


x = threading.Thread(target=calculate, args=())
x.start()

y = threading.Thread(target=message, args=())
y.start()

z = threading.Thread(target=do_something, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
