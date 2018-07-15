import statix.descriptive as d
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(data))

print()

print("statix mean:", d.mean(data))
print("statix var:", d.var(data))
print("statix std:", d.std(data))

print("numpy mean:", d.mean(data))
print("numpy var:", d.var(data))
print("numpy std:", d.std(data))

print()

print(d.median(data))
print(np.median(data))

print(d.get_range(data))