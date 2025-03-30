import matplotlib.pyplot as plt
import numpy as np

from os import listdir
from os.path import isfile, join


def print_results(filename):
    f = open(filename)
    x, y = [], []
    for i in range(3):
        n = f.readline()
        x.append(int(n))
        aver = [float(next(f).strip()) for _ in range(100)]
        y.append(sum(aver)/len(aver))
    print(filename+":"+str(y))
    f.close()


all_data_files = [f for f in listdir("research") if isfile(join("research", f))]

for fn in all_data_files:
    print_results("research/"+fn)
