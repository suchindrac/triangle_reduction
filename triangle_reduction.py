import math
import sys
import os
import argparse
from struct import *
import numpy as np
from decimal import Decimal

def get_d(a, b, c):
    if isinstance(a, str):
        a = ord(a) % 10
    else:
        a = a % 10
    if isinstance(b, str):
        b = ord(b) % 10
    else:
        b = b % 10
    if isinstance(c, str):
        c = ord(c) % 10
    else:
        c = c % 10

    a_2 = a * a
    b_2 = b * b
    third = 2 * a * b * math.cos(c)
    d_2 = a_2 + b_2 - third
    d = math.sqrt(abs(d_2))
    d = d % 10

    return d

def zip_it(inp):
    if len(inp) % 3 != 0:
        for i in range(len(inp) % 3):
            inp.append(0)

    i = 0

    comp = []
    while i <= len(inp) - 3:
        a = inp[i]
        b = inp[i + 1]
        c = inp[i + 2]

        d = get_d(a, b, c)

        comp.append(d)

        i += 3

    return comp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", type = str, required = True, help = "Input file")
    args = parser.parse_args()

    file = args.input_file
    here_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(here_path, file)
    with open(file_path, 'r') as fd:
        content = fd.read()

    content = [ord(x) for x in content]
    comp = zip_it(content)

    num_runs = 1
    while len(comp) != 1:
        comp = zip_it(comp)
        num_runs += 1

    print("Final compressed value: ", comp[0])
    print("Number of runs: ", num_runs)
