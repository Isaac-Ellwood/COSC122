import doctest 

def doubler(n):
    """ Returns double n, ie, 2*n
    >>> doubler(2)
    4
    >>> doubler(10)
    20
    >>> doubler('wow')
    'wowwow'
    """
    return 2*n

doctest.run_docstring_examples(doubler, globs=None)

# or use the following to run the doctests 
# in all docstrings in the module
# doctest.testmod()