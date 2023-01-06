# sortexample.py

""" example of how sorting works in python """

from quickiebase.butil import *

import functools

#---------------------------------------------------------------------

@printargs
def getTypeInt(x) -> int:
    """ return an int for a type """
    if isinstance(x, type(None)): return 1

    # must test for bool before int because a bool is an int
    if isinstance(x, bool): return 6

    if isinstance(x, (int, float)): return 2
    if isinstance(x, str): return 3
    if isinstance(x, dict): return 4
    if isinstance(x, list): return 5

    #anything else:
    return 7

@printargs
def xcmp(x, y) -> int:
    """ extended comparison function -- compares x and y of any types """

    tx = getTypeInt(x)
    ty = getTypeInt(y)
    if tx<ty: return -1
    if tx>ty: return 1

    # same type
    if tx in (4,5,7):
        # compare reprs
        rx = repr(x)
        ry = repr(y)
        if rx<ry: return -1
        if rx>ry: return 1
    else:
        if x<y: return -1
        if x>y: return 1
    return 0


if __name__=='__main__':
    a = ['foo', 'bar', [44,33], 2, True, False, None, {'x':15}]
    b = sorted(a, key=functools.cmp_to_key(xcmp))
    prn("a=%r b=%r", a, b)



#end
