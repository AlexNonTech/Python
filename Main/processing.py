import time
from multiprocessing import Process, cpu_count

def count(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=count, args=(125000000,))
    b = Process(target=count, args=(125000000,))
    c = Process(target=count, args=(125000000,))
    d = Process(target=count, args=(125000000,))
    e = Process(target=count, args=(125000000,))
    f = Process(target=count, args=(125000000,))
    g = Process(target=count, args=(125000000,))
    h = Process(target=count, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()


if __name__ == "__main__":
    main()

print('resulting time is ' + str(time.perf_counter()))