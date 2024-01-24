import random
import time


def shuffled():
    start_list = list(range(10000 + 1))
    shuffle = []
    while start_list:
        rand = random.randint(0, len(start_list) - 1)
        shuffle.append(start_list.pop(rand))
    return shuffle


def csort(raw_data):
    raw_data = list(raw_data)
    s = []
    for i in range(len(raw_data)):
        minimum = min(raw_data)
        raw_data.pop(raw_data.index(minimum))
        s.append(minimum)

    return s


if __name__ == '__main__':
    eg = shuffled()
    s2 = time.time()
    sorted_eg2 = sorted(eg)
    e2 = time.time()
    diff2 = e2 - s2
    print(f"standard time: {diff2}")
    s1 = time.time()
    sorted_eg = csort(eg)
    e1 = time.time()
    diff1 = e1 - s1
    print(f"custom time: {diff1}")

