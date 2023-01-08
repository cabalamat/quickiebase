# test_sorting.py = test <sorting.py>


from quickiebase.butil import *
from quickiebase import lintest

from quickiebase.quickietypes import *
from quickiebase import sorting
from quickiebase.sorting import normaliseSort, sortDocs, SortSpec

#---------------------------------------------------------------------

class T_normaliseSort(lintest.TestCase):

    """ Test the normaliseSort() function """

    def nsTest(self, f, sb):
        r = normaliseSort(f)
        self.assertSame(r, sb, form("%r -> %r", f, sb))

    def test_None(self):
        self.nsTest(None, [])


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

js1 = {
    "001": {"name": "Foo"},
    "002": {"name": "Bar"},
    "003": {"name": "Baz"},
}

class T_sortDocs(lintest.TestCase):
    """ the sortDocs() function """

    def sdTest(self,
        idDoc: IdDictJsonDoc,
        ss: SortSpec,
        sb: List[IdJsonDoc]
    ):
        r = sortDocs(idDoc, ss)
        self.assertSame(r, sb)

    def test_1(self):
        sb1 = [
            ("002", {"name": "Bar"}),
            ("003", {"name": "Baz"}),
            ("001", {"name": "Foo"}),
        ]
        self.sdTest(js1, "name", sb1)
        self.sdTest(js1, ("name",-1), sb1[::-1])

    def test_different_types(self):
        """ Comparison of values of different types """
        js = {
            "001": {"v": 34},
            "002": {"v": -3.5},
            "003": {"v": True},
            "004": {"v": False},
            "005": {"v": "foo"},
            "006": {"v": []},
            "007": {"v": {}},
            "008": {"v": None},
            "009": {"v": "foo"},
        }
        sb = [
            ("008", {"v": None}),
            ("002", {"v": -3.5}),
            ("001", {"v": 34}),
            ("005", {"v": "foo"}),
            ("009", {"v": "foo"}),
            ("007", {"v": {}}),
            ("006", {"v": []}),
            ("004", {"v": False}),
            ("003", {"v": True}),
        ]
        self.sdTest(js, [("v",1)], sb)




#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_normaliseSort)
group.add(T_sortDocs)

if __name__=='__main__': group.run()


#end
