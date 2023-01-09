# test_dbmdb.py = test <dbmdb.py>

""" test <dbmdb.py>

DbmDb and DbmCollection implement a database over dbm.
"""

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

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_DbmDb)

if __name__=='__main__': group.run()


#end
