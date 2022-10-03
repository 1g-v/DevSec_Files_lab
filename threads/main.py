import string
import multiprocessing as mp
from hashlib import sha256
import itertools
import time

alphabet = string.ascii_lowercase
with open("sha.txt") as file:
    array = [row.strip() for row in file]


def f(alphabet_bit):
    for i in itertools.product(alphabet_bit, alphabet, alphabet, alphabet, alphabet):
        if sha256(''.join(i).encode('utf-8')).hexdigest() in array:
            print('Password for the hash function ' + sha256(''.join(i).encode('utf-8')).hexdigest() + ' - ' + ''.join(i))


if __name__ == '__main__':
    procs = []
    proc_count = int(input("enter proc count - "))
    parts_count = len(alphabet) // proc_count
    for i in range(proc_count):
        if i == proc_count - 1:
            bit = alphabet[-1]
        else:
            bit = alphabet[parts_count * i:parts_count * (i + 1)]
        p = mp.Process(target=f, args=(bit,))
        procs.append(p)
        p.start()
    [proc.join() for proc in procs]