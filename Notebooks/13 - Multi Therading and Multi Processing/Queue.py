import multiprocessing

def even_no(num, n):
    for i in num:
        if i % 2 == 0:
            n.put(i)

if __name__ == "__main__":
    n = multiprocessing.Queue()
    p = multiprocessing.Process(target=even_no, args=(range(10), n))
    p.start()
    p.join()

    while n:
        print(n.get())  