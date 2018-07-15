def mean(data, type='Average'):
    """Calculate and return the mean value of the data."""
    average = 0
    for val in data:
        average += val
    return (average/len(data))

