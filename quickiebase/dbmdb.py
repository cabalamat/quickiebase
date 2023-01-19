# dbmdb.py = Database implemented on dbm

""" dbmdb
    =====

DbmDb and DbmCollection implement a database over dbm.
"""

from typing import List, Tuple, Union, Dict, Optional, Any, Iterator
import dbm
import json

from . import butil
from .butil import form

from .quickietypes import DocId, JsonDoc

from .gendb import GenDb, GenCollection
from .ramdb import RamDb, RamCollection, removeId

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

    def makeCollection(self, colName: str):
        """ create a new collection in this database """
        newCol = DbmCollection(self, colName)
        self.collections[colName] = newCol


#---------------------------------------------------------------------

def toJsonCompact(jd:JsonDoc) -> str:
    jStr = json.dumps(jd, separators=(',', ':'), sort_keys=True)
    return jStr


def s2b(id: DocId) -> bytes:
    """ convert a document id (a str) into bytes, for dbm """
    b = bytes(id, "utf-8")
    return b


def j2b(jd: JsonDoc) -> bytes:
    """ convert a document (a JsonDoc) into bytes, for dbm """
    jStr = toJsonCompact(jd)
    b = bytes(jStr, "utf-8")
    return b


class DbmCollection(RamCollection):

    db: DbmDb
    name: str = ""
    pan: str # full pathname to my file
    documents: Dict[DocId, JsonDoc] = {}
    inRam: bool = False # documents currently in RAM

    def __init__(self, db: DbmDb, name: str):
        self.db = db
        self.name = name
        self.documents = {}
        self.inRam = False
        self.pan = butil.join(db.dbDir, name)
        self.ud = dbm.open(self.pan, 'c')

    def delete_one(self, id: DocId):
        """ delete a document based on its id """
        keyU = s2b(id)
        if keyU in self.ud:
            del self.ud[keyU]
        if self.inRam:
            self.documents.pop(id, None)

    def insert_one(self, jDoc: JsonDoc):
        """ save a document, where the document has an id.
        It might be a new document or over-write an existing one
        """
        if "_id" in jDoc and isinstance(jDoc['_id'], DocId):
            id = jDoc["_id"]
        else:
            id = self.makeNewId()
        j2 = removeId(jDoc)
        keyU = s2b(id)
        self.ud[s2b(id)] = j2b(j2)
        if self.inRam:
           self.documents[id] = j2

    def saveToFile(self, pan: str):
        """ save to the file (pan), where pan is the full pathname """
        self._ensureInRam()
        super().saveToFile(pan)

    def saveToFilePretty(self, pan: str):
        """ save to the file (pan), where pan is the full pathname """
        self._ensureInRam()
        super().saveToFilePretty(pan)

#---------------------------------------------------------------------

#end
