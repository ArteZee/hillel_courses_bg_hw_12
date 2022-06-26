# Applies the specified function to an element of the sequence, reducing it to a single connection.

def reduce(function, iterable, initializer=None):
    """
    Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
    :param function:
    :param iterable:
    :param initializer:
    :return:
    """
    #  create iter argument e
    it = iter(iterable)
    # if we don`t have initializer(start) we set value == first element in iterable
    if initializer is None:
        value = next(it)
    #  if we have initializer(start) we set it to value and do our function to him
    else:
        value = initializer
    # cycle set value to function result
    for element in it:
        value = function(value, element)
    return value


print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
