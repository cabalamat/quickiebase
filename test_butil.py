# test_butil.py = tests <butil.py>

from quickiebase.butil import *
from quickiebase import lintest

#---------------------------------------------------------------------

class T_miscFunctions(lintest.TestCase):

    def test_kv(self):
        """ kv() returns a list of key-value pairs """

        r = list(kv([]))
        sb = []
        self.assertSame(r, sb, "empty list")

        r = list(kv(['cc', 'vvv', 'alpha']))
        sb = [(0,'cc'), (1,'vvv'), (2,'alpha')]
        self.assertSame(r, sb, "list")

        r = list(kv({}))
        sb = []
        self.assertSame(r, sb, "empty dict")

        r = list(kv({'a':4, 'b':'zz'}))
        sb = [('a',4), ('b','zz')]
        self.assertSame(r, sb, "dict")

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_miscFunctions)

if __name__=='__main__': group.run()

#end
