# test_dbmdb.py = test <dbmdb.py>

""" test <dbmdb.py>

DbmDb and DbmCollection implement a database over dbm.
"""

import dbm

from quickiebase.butil import *
from quickiebase import lintest

from quickiebase.quickietypes import *
from quickiebase import dbmdb
from quickiebase.dbmdb import DbmDb, DbmCollection

#---------------------------------------------------------------------

class T_DbmDb(lintest.TestCase):

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

    def test_fileCreation(self):
        """ does it create a directory for a database? """
        db = DbmDb("mybase")
        self.assertDirExists("~/.local/share/dbmdb/mybase")

    def test_colCreation(self):
        db = DbmDb("mybase")
        col = db.getCollection("mycol")

        col.insert_one({'_id':"001", 'v':55, 'n':"cat"})
        col.insert_one({'_id':"002", 'v':41, 'n':"dog"})

        raw = col.ud
        for k in raw.keys():
            prn("key %r:", k)
            value = raw[k]
            prn("    %r", value)
        #//for k




#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_DbmDb)

if __name__=='__main__': group.run()


#end
