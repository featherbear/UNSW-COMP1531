'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):
    '''
    >>> calculate("1+3")
    4
    >>> calculate("1+3*4/3")
    5.0
    >>> calculate("(1+3)*5")
    20
    >>> calculate("-----1")
    -1
    >>> calculate("-+-1")
    1
    >>> calculate(\'print("bad guy coming to hack")\')
    '''
    import re
    return eval(s) if re.search("^[0-9+\-*/() ]*$", s) else None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
