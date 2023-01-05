# test_sorting.py = test <sorting.py>


from quickiebase.butil import *
from quickiebase import lintest

from quickiebase import sorting

#---------------------------------------------------------------------

class T_normaliseSort(lintest.TestCase):

    """ Test the normaliseSort() function """


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_normaliseSort)
#group.add(T_sortDocs)

if __name__=='__main__': group.run()


#end
