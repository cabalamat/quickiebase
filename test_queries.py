# test_queries.py = test <queries.py>


from quickiebase.butil import *
from quickiebase import lintest

from quickiebase.quickietypes import JsonDoc
from quickiebase import queries
from quickiebase.queries import QuerySpec

#---------------------------------------------------------------------
# data

doc = {
   'name': 'exxample',
   'email': 'exxam@example.com',
   'valid': True,
   'size': 123,
}

#---------------------------------------------------------------------

class T_queries(lintest.TestCase):

    def tq(self, doc: JsonDoc, q: QuerySpec, sb: bool):
        """ Test a query.
        (doc) is the document, (q) is the query, and
        (sb) is whether the document should match the query
        """
        m = queries.matchesQuery(doc, q)
        if m==sb:
            self.passed(form("Document %r\n  %s query %r",
                doc,
                "matches" if m else "doesn't match",
                q))
        else:
            if m:
                matchS = "matches"
                shouldS = "shouldn't"
            else:
                matchS = "doesn't match"
                shouldS = "should"
            self.failed(form("Document %r\n  %s query %r,\nbut it %s",
                doc, matchS, q, shouldS))

    def test_nullQuery(self):
        m = queries.matchesQuery(doc, None)
        self.assertTrue(m, "doc matches None")

    def test_emptyQuery(self):
        m = queries.matchesQuery(doc, {})
        self.assertTrue(m, "doc matches {}")

    def test_missingField(self):
        """ the field in the query doesn't exist in the doucment,
        so should return false
        """
        m = queries.matchesQuery(doc, {'foo':'bar'})
        self.assertFalse(m, "doc doesn't match")

    def test_equal(self):
        """ test for equality of fields """
        self.tq(doc, {'name': 'exxample'}, True)
        self.tq(doc, {'name': 'zzzzz'}, False)

    def test_equal_multi(self):
        """ test for equality on multiple fields """
        self.tq(doc, {'name':'exxample', 'size':123}, True)
        self.tq(doc, {'name':'exxample', 'foo':'bar'}, False)
        self.tq(doc, {'name':'exxample', 'valid':False}, False)

    def test_comparisonOperators(self):
        """ the operators: $gt $gte $lt $lte $eq $ne """
        self.tq(doc, {'size': {'$gt': 122}}, True)
        self.tq(doc, {'size': {'$gt': 123}}, False)
        self.tq(doc, {'size': {'$gt': 124}}, False)

        self.tq(doc, {'size': {'$gte': 122}}, True)
        self.tq(doc, {'size': {'$gte': 123}}, True)
        self.tq(doc, {'size': {'$gte': 124}}, False)

        self.tq(doc, {'email': {'$lt': 'aaa'}}, False)
        self.tq(doc, {'email': {'$lt': 'exxam@example.com'}}, False)
        self.tq(doc, {'email': {'$lt': 'zzz'}}, True)

        self.tq(doc, {'email': {'$lte': 'aaa'}}, False)
        self.tq(doc, {'email': {'$lte': 'exxam@example.com'}}, True)
        self.tq(doc, {'email': {'$lte': 'zzz'}}, True)

        self.tq(doc, {'valid': {'$eq': True}}, True)
        self.tq(doc, {'valid': {'$ne': True}}, False)

        self.tq(doc, {'name': {'$eq': 'xxxx'}}, False)
        self.tq(doc, {'name': {'$ne': 'xxxx'}}, True)

    def test_inNinOperators(self):
        """ the $in and $nin operators """
        self.tq(doc, {'name': {'$in': ['exxample']}}, True)
        self.tq(doc, {'name': {'$in': ['exxample','red']}}, True)
        self.tq(doc, {'name': {'$in': ['green','red']}}, False)
        self.tq(doc, {'name': {'$in': []}}, False)

        self.tq(doc, {'name': {'$nin': ['exxample']}}, False)
        self.tq(doc, {'name': {'$nin': ['exxample','red']}}, False)
        self.tq(doc, {'name': {'$nin': ['green','red']}}, True)
        self.tq(doc, {'name': {'$nin': []}}, True)

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_queries)

if __name__=='__main__': group.run()



#end
