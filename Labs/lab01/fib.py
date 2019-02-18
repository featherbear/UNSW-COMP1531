'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    result = []
    if n >= 1: result.append(1)
    if n >= 2: result.append(1)

    i = 2
    while i < n:
      result.append(result[i-1] + result[i-2])
      i += 1

    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
