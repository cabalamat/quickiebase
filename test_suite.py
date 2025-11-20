# test_suite.py

"""
This is a suite of regression tests for databases to perform

"""


from abc import ABC, abstractmethod
import dbm

from quickiebase.butil import *
from quickiebase import lintest

from quickiebase.quickietypes import *
from quickiebase import gendb, dbmdb
from quickiebase.dbmdb import DbmDb, DbmCollection

#---------------------------------------------------------------------

class T_creation(lintest.TestCase):

    """ create a database and collaction and add saome documents to it. """

    def test_createDB(self):
        """ create a database """
        self.db = dbmdb.DbmDb("suite")
        self.assertTrue(isinstance(self.db, gendb.GenDb),
            "created a Db")

    def test_createCol(self):
        """ create a collection """
        self.col = self.db.getCollection("mycol")
        self.assertTrue(isinstance(self.col, gendb.GenCollection),
            "created a Collection")
        self.assertSame(self.col.name, "mycol", "collection knows its name")

    def test_saveDoc(self):
        """ the saveDoc() function """
        j1 = {'_id':"001", "name": "foo", "species": "dog"}
        self.col.insert_one(j1)
        r = self.col.count()
        self.assertSame(r, 1, "1 document in mycol")

        j2 = {'_id':"002", "name": "flopsy", "species": "rabbit"}
        self.col.insert_one(j2)
        r = self.col.count()
        self.assertSame(r, 2, "2 documents in mycol")

        j3 = {'_id':"003", "name": "felix", "species": "cat"}
        self.col.insert_one(j3)
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
