import statix.descriptive as d
import numpy as np

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nSorted Data:\t", sorted(data), "\n")

print("Statix mean:\t", d.mean(data), end='\t\t')
print("Numpy mean:\t\t", np.mean(data))
print("Statix median:\t", d.median(data), end='\t\t')
print("Numpy median:\t", np.median(data))
print("Statix var:\t\t", d.var(data), end='\t\t')
print("Numpy var:\t\t", np.var(data))
print("Statix std:\t\t", round(d.std(data), ndigits=3), end='\t\t')
print("Numpy std:\t\t", round(np.std(data), ndigits=3))

print()

print("Statix range:\t\t\t", d.get_range(data))
print("Statix 75th percentile:\t", d.percentile(data, 75))
print("Statix 0.75 quantile:\t", d.quantile(data, 0.75))
print("Statix IQR:\t\t\t\t", d.iqr(data))