def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def check_reduce(function, iterable, initializer=None):
    """
    function checking if we have value in iterable
    if not - put explanation
    :param function:
    :param iterable:
    :param initializer:
    :return: error if iterable have not value
    """
    # check that iterable  not empty
    assert len(iterable) != 0, f"Your iterable have not value"


check_reduce(lambda x, y: x * y, [])
