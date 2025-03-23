import matplotlib.pyplot as plt
import numpy as np


# 2.2416114807128905e-05, 1.446247100830078e-05, 3.197193145751953e-05
f = open("research/insert.txt")
x, y = [], []
for i in range(3):
    n = f.readline()
    x.append(int(n))
    aver = [float(next(f).strip()) for _ in range(100)]
    y.append(sum(aver)/len(aver))
print(y)

# 4.783153533935547e-05, 0.00043350934982299804, 0.012225885391235352
f = open("research/delete.txt")
x, y = [], []
for i in range(3):
    n = f.readline()
    x.append(int(n))
    aver = [float(next(f).strip()) for _ in range(100)]
    y.append(sum(aver)/len(aver))
print(y)

# 3.793478012084961e-05, 0.00028342247009277344, 0.010575106143951416
f = open("research/update.txt")
x, y = [], []
for i in range(3):
    n = f.readline()
    x.append(int(n))
    aver = [float(next(f).strip()) for _ in range(100)]
    y.append(sum(aver)/len(aver))
print(y)

# 5.687713623046875e-05, 0.0001582479476928711, 0.0016176605224609375
f = open("research/selectkey.txt")
x, y = [], []
for i in range(3):
    n = f.readline()
    x.append(int(n))
    aver = [float(next(f).strip()) for _ in range(100)]
    y.append(sum(aver)/len(aver))
print(y)

# 6.318092346191406e-05, 0.0002146792411804199, 0.001925656795501709
f = open("research/selectnokey.txt")
x, y = [], []
for i in range(3):
    n = f.readline()
    x.append(int(n))
    aver = [float(next(f).strip()) for _ in range(100)]
    y.append(sum(aver)/len(aver))
print(y)