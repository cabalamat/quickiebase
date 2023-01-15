# dbmdb.py = Database implemented on dbm

""" dbmdb
    =====

DbmDb and DbmCollection implement a database over dbm.
"""

from typing import List, Tuple, Union, Dict, Optional, Any, Iterator

from . import butil
from .butil import form

from .quickietypes import DocId, JsonDoc

from .gendb import GenDb, GenCollection
from .ramdb import RamDb, RamCollection

#---------------------------------------------------------------------

def validName(s: str) -> bool:
    """ Is (s) a valid database or collection name? """
    firstChar = "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    restChars = firstChar + "0123456789"
    if len(s)<1: return False
    if s[0] not in firstChar: return False
    return all(c in restChars for c in s[1:])

#---------------------------------------------------------------------

DEFAULT_BASE_DIR = "~/.local/share/dbmdb/"

class DbmDb(RamDb):
    """ a local database, in RAM """

    dbName: str = ""
    dbDir: str = ""

    def __init__(self, dbName:str):
        """ create a database, optionally saying which directory it's in """
        self.dbName = dbName
        self.dbDir = butil.join(DEFAULT_BASE_DIR, dbName)
        butil.createDir(self.dbDir)

    def getCollection(self, colName: str) -> 'DbmCollection':
        """ return a collection in this database, creating it if
        necessary
        """

#---------------------------------------------------------------------

class DbmCollection(RamCollection):
    pass


#---------------------------------------------------------------------

#end
