# test_ramdb.py = test <ramdb.py>

from quickiebase.butil import *
from quickiebase import lintest

from quickiebase.quickietypes import JsonDoc
from quickiebase.queries import QuerySpec

from quickiebase import ramdb

#---------------------------------------------------------------------

class T_creation(lintest.TestCase):

    """ create a database and collaction and add saome documents to it. """

    def test_createDB(self):
        """ create a database """
        self.db = ramdb.RamDb()
        self.assertTrue(isinstance(self.db, ramdb.RamDb),
            "created a RamDb")

    def test_createCol(self):
        """ create a collection """
        self.col = self.db.getCollection("mycol")
        self.assertTrue(isinstance(self.col, ramdb.RamCollection),
            "created a RamCollection")
        self.assertSame(self.col.name, "mycol", "collection knows its name")

    def test_saveDoc(self):
        """ the saveDoc() function """
        j1 = {'_id':"001", "name": "foo", "species": "dog"}
        self.col.saveDoc(j1)
        r = self.col.count()
        self.assertSame(r, 1, "1 document in mycol")

        j2 = {'_id':"002", "name": "flopsy", "species": "rabbit"}
        self.col.saveDoc(j2)
        r = self.col.count()
        self.assertSame(r, 2, "2 documents in mycol")

        j3 = {'_id':"003", "name": "felix", "species": "cat"}
        self.col.saveDoc(j3)
        r = self.col.count()
        self.assertSame(r, 3, "3 documents in mycol")
        prn("self.col=%s", self.col)

    def test_getDoc(self):
        """ get documents based on id """
        j = self.col.getDoc("001")
        self.assertSame(j, {'_id':"001", "name": "foo", "species": "dog"})

        j = self.col.getDoc("002")
        self.assertSame(j, {'_id':"002", "name": "flopsy", "species": "rabbit"})

        j = self.col.getDoc("003")
        self.assertSame(j, {'_id':"003", "name": "felix", "species": "cat"})

    def test_delete_one(self):
        """ delete documents based on id """
        self.col.delete_one("001")
        r = self.col.count()
        self.assertSame(r, 2, "doc 001 deleted, now 2 documents in mycol")

        self.col.delete_one("001")
        r = self.col.count()
        self.assertSame(r, 2, "deleting it again does nothing")

        self.col.delete_one("im-not-here")
        r = self.col.count()
        self.assertSame(r, 2, "deleting non-existant document does nothing")

        self.col.delete_one("003")
        r = self.col.count()
        self.assertSame(r, 1, "doc 003 deleted, only 1 left now")
        j = self.col.getDoc("002")
        self.assertSame(j, {'_id':"002", "name": "flopsy", "species": "rabbit"},
            "rabbit still there")



#---------------------------------------------------------------------


#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_creation)

if __name__=='__main__': group.run()


#end
