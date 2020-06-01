def square(x):
    '''
    Multiply x by itself
    >>> [square(x) for x in range(5)]
    [0, 1, 4, 9, 16]
    >>> square(-2)
    4
    '''
    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()

