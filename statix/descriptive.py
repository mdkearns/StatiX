# Package: statix
# Module:  descriptive
# About:   A module for computing descriptive statistics.
# Author:  Matthew D. Kearns
# Contact: mattdkearns@gmail.com


from math import ceil, sqrt


def mean(data, trim=0, weights=None):
    """Calculate and return the mean value of the data.

    data: a python list-like object
    trim: [0, 1]; default=0
    weights: a python list-like object; default=None
    """

    average = 0

    if 0 < trim <= 1:                             # trim data
        trim_amt = ceil(trim*len(data))
        data = sorted(data)
        for i in range(trim_amt):
            data.pop(0)
            data.pop()
            if weights:
                weights.pop(0)
                weights.pop()

    if weights:                                  # if weighted, compute weighted average
        for i in range(len(data)):
            average += data[i] * weights[i]
    else:                                        # otherwise, compute normal average
        for val in data:
            average += val

    return average / len(data)


def var(data, isSample=False):
    """Compute and return variance of data.

    data: a python list-like object
    isSample: True/False; default=False
    """

    x_bar = mean(data)
    variance = 0

    for x in data:
        variance += ((x - x_bar)**2)

    if isSample:
        return variance / (len(data)-1)
    else:
        return variance / len(data)


def std(data, isSample=False):
    """Compute and return standard deviation of data.

    data: a python list-like object
    isSample: True/False; default=False
    """
    return sqrt(var(data, isSample))

def mad(data, isSample=False):
    """Compute and return mean-absolute-deviation.

    data: a python list-like object
    isSample: True/False; default=False
    """

    x_bar = mean(data)
    mad = 0

    for x in data:
        mad += abs(x - x_bar)

    if isSample:
        return mad / (len(data) - 1)
    else:
        return mad / len(data)


# create function aliases
mse = var
mean_squared_error = var
variance = var
l2_norm = std
euclidean_norm = std
mean_absolute_deviation = mad
l1_norm = mad
manhattan_distance = mad