import statix.descriptive as d

data = [1, 2, 3, 4, 5]

print(sorted(data))

print(d.mean(data, weights=[1, 2, 3, 3, 4]))