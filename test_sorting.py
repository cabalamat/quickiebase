# test_sorting.py = test <sorting.py>


from quickiebase.butil import *
from quickiebase import lintest

from quickiebase import sorting
from quickiebase.sorting import normaliseSort, sortDocs

#---------------------------------------------------------------------

class T_normaliseSort(lintest.TestCase):

    """ Test the normaliseSort() function """

    def nsTest(self, f, sb):
        r = normaliseSort(f)
        self.assertSame(r, sb, form("%r -> %r", f, sb))

    def test_None(self):
        self.nsTest(None, None)


    def test_str(self):
        self.nsTest("foo", [("foo", 1)])
        self.nsTest(["foo", "bar"],
                    [("foo", 1), ("bar", 1)])

    def test_oneColumn(self):
        self.nsTest(("foo", -1),
                    [("foo", -1)])

    def test_multiColumn(self):
        self.nsTest(  [('foo',-1), 'bar'],
                      [('foo',-1), ('bar',1)]  )

        self.nsTest(  [('foo',-1), 'bar', 'baz'],
                      [('foo',-1), ('bar',1), ('baz',1)]  )


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_normaliseSort)
#group.add(T_sortDocs)

if __name__=='__main__': group.run()


#end
