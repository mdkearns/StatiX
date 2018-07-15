import statix.descriptive as d
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(data))

print()

print("statix mean:\t", d.mean(data))
print("statix median:\t", d.median(data))
print("statix var:\t", d.var(data))
print("statix std:\t", round(d.std(data), ndigits=3))

print()

print("numpy mean:\t", np.mean(data))
print("numpy median:\t", np.median(data))
print("numpy var:\t", np.var(data))
print("numpy std:\t", round(np.std(data), ndigits=3))

print(d.get_range(data))