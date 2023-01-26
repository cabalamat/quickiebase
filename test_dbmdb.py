# test_dbmdb.py = test <dbmdb.py>

""" test <dbmdb.py>

DbmDb and DbmCollection implement a database over dbm.
"""

import shutil

from quickiebase import butil

import dbm

from quickiebase.butil import *
from quickiebase import lintest

from quickiebase.quickietypes import *
from quickiebase import dbmdb
from quickiebase.dbmdb import DbmDb, DbmCollection

#---------------------------------------------------------------------

class T_validName(lintest.TestCase):

    def test_validName(self):
        """ validName() """
        r = dbmdb.validName("")
        self.assertFalse(r, ' "" is invalid')

        r = dbmdb.validName("_")
        self.assertTrue(r, ' _ is valid')

        r = dbmdb.validName("xyz")
        self.assertTrue(r, ' xyz is valid')

        r = dbmdb.validName("0xyz")
        self.assertFalse(r, ' 0xyz is invalid')

        r = dbmdb.validName("the bad name")
        self.assertFalse(r, ' "the bad name"" is invalid')

#---------------------------------------------------------------------

class T_DbmDb(lintest.TestCase):
    """ test the creation of dbm's files and directories """

    def setUpAll(self):
        dbDir = butil.join("~/.local/share/dbmdb/mybase")
        shutil.rmtree(dbDir, ignore_errors=True)
        self.assertDirDoesNotExist(dbDir)

        butil.deleteFile("mybase.json")
        self.assertFileDoesNotExist("mybase.json")

        butil.deleteFile("mybasep.json")
        self.assertFileDoesNotExist("mybasep.json")


    def test_fileCreation(self):
        """ does it create a directory for a database? """
        db = DbmDb("mybase")
        self.assertDirExists("~/.local/share/dbmdb/mybase")

    def test_colCreation(self):
        self.db = DbmDb("mybase")
        self.assertSame(self.db.__class__, DbmDb,
             "(db) is a DbmDb")
        col = self.db.getCollection("mycol")
        self.assertSame(col.__class__, DbmCollection,
             "(col) is a DbmCollection")

        col.insert_one({'_id':"001", 'v':55, 'n':"cat"})
        col.insert_one({'_id':"002", 'v':41, 'n':"dog"})
        prn("=== Contents of dbm database: ===")
        raw = col.ud
        for k in raw.keys():
            prn("key %r:", k)
            value = raw[k]
            prn("    %r", value)
        #//for k

        #col.saveToFile("mybase.json")
        #self.assertFileExists("mybase.json")

        #col.saveToFilePretty("mybasep.json")
        #self.assertFileExists("mybasep.json")

    def test_getDoc(self):
        col = self.db.getCollection("mycol")
        r = col.getDoc("001")
        self.assertSame(r, {'_id':"001", 'v':55, 'n':"cat"})

        r = col.getDoc("002")
        self.assertSame(r, {'_id':"002", 'v':41, 'n':"dog"})

        r = col.getDoc("003")
        self.assertSame(r, None)





#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_validName)
group.add(T_DbmDb)

if __name__=='__main__': group.run()


#end
