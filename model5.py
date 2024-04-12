import numpy as np

p1 = 0.97 * np.array([0.45, 0.07, 0.12, 0.27])
s1 = 0.95 * np.array([0.12, 0.38, 0.25, 0.4])
m1 = 0.9 * np.array([0.04, 0.01, 0.02, 0.03])
total_percent = 1.05
pw1 = 0.22 * total_percent
sw1 = 0.3 * total_percent
mw1 = 0.02 * total_percent
sw2 = 0.3 * total_percent
profit_percent = 1.05 - 0.68
print(f"p1/pw1: {p1 - pw1}")
print(f"s1/sw1: {s1 - sw1}")
print(f"m1/mw1: {m1 - mw1}")
