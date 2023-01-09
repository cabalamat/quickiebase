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

    def test_fileCreation(self):
        """ does it create directory for a database """
        db = DbmDb("mybase")
        self.assertDirExists("~/.local/share/dbmdb/mybase")

#---------------------------------------------------------------------

group = lintest.TestGroup()
group.add(T_DbmDb)

if __name__=='__main__': group.run()


#end
