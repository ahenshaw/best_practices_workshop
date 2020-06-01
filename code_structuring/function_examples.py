def fn(a, b=[]):
    ''' 
    Intent: create a new list (if one isn't passed in), 
    initialize with the value passed in as "a".
    '''
    b.append(a)
    return b

print(fn(1))
print(fn(2))

print(fn.__doc__)


def fn(a, b=None):
    ''' 
    Intent: create a new list (if one isn't passed in), 
    initialize with the value passed in as "a".
    '''
    if b is None:
        b = []
    b.append(a)
    return b

print(fn(1))
print(fn(2))


def variadic(*params):
    print(params)
    print(params[0])

variadic(1,2,3)


def varargs(**kwargs):
    print(kwargs)
    print(kwargs['a'])

varargs(a=1, b=2, c=3)