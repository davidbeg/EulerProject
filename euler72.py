import multiprocessing
from threading import Thread
from time import time, sleep

from matplotlib.pyplot import plot, show


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def find_factors(number):
    factors = set()
    factor = 2
    while number > 1:
        if number % factor == 0:
            factors.add(factor)
            number /= factor
        else:
            factor += 1
    return factors


PROCESSES = 8


def func(arg):
    num = arg
    print("Start for " + str(num))
    count = 0
    lim = 10 ** 6
    t = time()
    while num <= lim:
        factors = find_factors(num)
        x = num
        for factor in factors:
            x //= factor
        for factor in factors:
            x *= (factor - 1)
        num += PROCESSES
        count += x
        if num % (lim / 20) < PROCESSES:
            print("\n" + ("\t\t\t\t\t" * (arg - 2)) + "Thead number " + str(arg) + " :", end="")
            print(str(int(num / (lim / 100))), end="%: ")
            print("{:.2f}".format(time() - t))
            t = time()
    print("+++++++++++++++++++++COUNT: " + str(count))


if __name__ == '__main__':
    ps = []
    all_time = time()
    for i in range(2, 2 + PROCESSES):
        p = multiprocessing.Process(target=func, args=(i,))
        p.start()
        ps.append(p)
        sleep(0.1)
    for p in ps:
        p.join()
    print("All time: " + str(time() - all_time))

