import statix.descriptive as d

data = [1, 3, 5, 5, 5, 2, 0, 0, 1, 9, 8, 9, 8, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(sorted(data))

print(d.mean(data, trim=0.1))