# Package: statix
# Module:  descriptive
# About:   A module for computing descriptive statistics.
# Author:  Matthew D. Kearns
# Contact: mattdkearns@gmail.com


from math import ceil, floor, modf, sqrt


def mean(data, trim=0, weights=None):
    """Calculate and return the mean value of the data.

    data: a python list-like object
    trim: [0, 1]; default=0
    weights: a python list-like object; default=None
    """

    average = 0

    if 0 < trim <= 1:  # trim data
        trim_amt = ceil(trim * len(data))
        data = sorted(data)
        for i in range(int(trim_amt)):
            data.pop(0)
            data.pop()
            if weights:
                weights.pop(0)
                weights.pop()

    if weights:  # if weighted, compute weighted average
        for i in range(len(data)):
            average += data[i] * weights[i]
    else:  # otherwise, compute normal average
        for val in data:
            average += val

    return average / len(data)


def median(data):
    """Find and return the median value."""

    data = sorted(data[:])

    if len(data) % 2 == 0:
        pop_amt = (len(data) // 2) - 1

        for i in range(pop_amt):
            data.pop(0)
            data.pop()

        m = (data[0] + data[1]) / 2

    else:
        pop_amt = (len(data) // 2)

        for i in range(pop_amt):
            data.pop(0)
            data.pop()

        m = data[0]

    return m


def var(data, is_sample=False):
    """Compute and return variance of data.

    data: a python list-like object
    isSample: True/False; default=False
    """

    x_bar = mean(data)
    v = 0

    for x in data:
        v += ((x - x_bar) ** 2)

    if is_sample:
        return v / (len(data) - 1)
    else:
        return v / len(data)


def std(data, is_sample=False):
    """Compute and return standard deviation of data.

    data: a python list-like object
    isSample: True/False; default=False
    """
    return sqrt(var(data, is_sample))


def mad(data, is_sample=False):
    """Compute and return mean-absolute-deviation.

    data: a python list-like object
    isSample: True/False; default=False
    """

    x_bar = mean(data)
    m = 0

    for x in data:
        m += abs(x - x_bar)

    if is_sample:
        return m / (len(data) - 1)
    else:
        return m / len(data)


def get_range(data):
    """Find and return the range."""

    return max(data) - min(data)


def percentile(data, k):
    """Calculate and return the kth percentile.

    data: a python list-like object
    k: the percentile
    """

    data = sorted(data[:])  # sort copy of data
    k_index = k * len(data) / 100  # get index of kth value
    frac, whole = modf(k_index)  # check if frac is > 0

    if frac > 0:
        per = data[int(floor(k_index))]
    else:
        per = (data[int(k_index)] + data[int(k_index) - 1]) / 2

    return per


def quantile(data, q):
    """Calculate and return the kth quantile.

    data: a python list-like object
    k: the quantile"""

    return percentile(data, q * 100)


def iqr(data):
    """Calculate and return the inter-quartile range."""

    return quantile(data, 75) - quantile(data, 25)


# create function aliases
mse = var
mean_squared_error = var
variance = var
l2_norm = std
euclidean_norm = std
mean_absolute_deviation = mad
l1_norm = mad
manhattan_distance = mad
