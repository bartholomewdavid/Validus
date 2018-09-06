import math

def daily_return(previous, current):
    """
    Calculate daily return on investment

    :param previous: The previous Mid
    :param current: The current Mid
    :return: The return on investment
    """
    return (current / previous) - 1

def average(inputs):
    """
    Returns the average value for the collection on inputs provided

    :param inputs: An iterable collection of Mids
    :return: The average

    """
    return (1.0 / len(inputs)) * sum(inputs)

def std_deviation(inputs):
    """
    Return the standard deviation from the collection of inputs provided

    :param inputs: AN iterable collection of Mids
    :return: The standard deviation
    """
    avg = average(inputs)
    duration = 1.0 / ((len(inputs) - 1.0))
    sigma = sum([pow((val - avg), 2) for val in inputs])

    return math.sqrt(duration * sigma)

def covariance(x_inputs, y_inputs):
    """
    Calculates the covariance between two collections of variables

    *Both collections must be of equal length*

    :param x_inputs: Collection x of Mids
    :param y_inputs: Collection y of Mids
    :return: The covariance value
    """
    # The collections must be the same length
    assert(len(x_inputs) == len(y_inputs))

    x_avg = average(x_inputs)
    y_avg = average(y_inputs)

    duration = 1.0 / ((len(x_inputs) - 1.0))
    sigma = sum([(x_inputs[i] - x_avg) * (y_inputs[i] - y_avg) for i in range(len(x_inputs))])

    return duration * sigma

def correlation(x_inputs, y_inputs):
    # The collections must be the same length
    assert(len(x_inputs) == len(y_inputs))

    cov = covariance(x_inputs, y_inputs)
    x_std = std_deviation(x_inputs)
    y_std = std_deviation(y_inputs)

    return cov / (x_std * y_std)