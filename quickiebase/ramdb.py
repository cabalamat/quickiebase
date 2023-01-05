# ramdb.py = a database in RAM


from typing import List, Tuple, Union, Dict, Optional, Any, Iterator
import json

from . import butil
from .butil import form

from .quickietypes import DocId, JsonDoc

from . import sorting
from .sorting import SortSpec

from . import queries
from .queries import QuerySpec

from .gendb import GenDb, GenCollection

#---------------------------------------------------------------------

class RamDb(GenDb):
    """ a local database, in RAM """

    collections: dict[str,'RamCollection'] = {}
    ix: int = 1 # index for document _id

    def getCollection(self, colName: str) -> 'RamCollection':
        """ return a collection in this database, creating it if
        necessary
        """
        if not colName in self.collections:
            self.makeCollection(colName)
        return self.collections[colName]

    def makeCollection(self, colName: str):
        """ create a new collection in this database """
        newCol = RamCollection(self, colName)
        self.collections[colName] = newCol

    def makeIdStub(self) -> str:
        """ make a stub for an id """
        self.ix += 1
        idStub = base36encode(self.ix)
        if len(idStub) < 4:
            idStub = "0"*(4-len(idStub)) + idStub
        return idStub

BASE_36_CHARS = "0123456789abcdefghijklmnopqrstuvwxyz"

def base36encode(n: int) -> str:
    """Converts an integer to a base36 string."""
    r = ''
    sign = ''
    if n < 0:
        sign = '-'
        n = -n

    if 0 <= n < len(BASE_36_CHARS):
        return sign + BASE_36_CHARS[n]
    while n != 0:
        n, i = divmod(n, len(BASE_36_CHARS))
        r = BASE_36_CHARS[i] + r

    return sign + r

#---------------------------------------------------------------------
# utility functions


def addId(doc: JsonDoc, id: DocId) -> JsonDoc:
    """ add an _id to a document """
    doc2 = doc.copy()
    doc2['_id'] = id
    return doc2

def removeId(doc: JsonDoc) -> JsonDoc:
    """ remove an id from a document """
    doc2 = doc.copy()
    doc2.pop("_id", None)
    return doc2

#---------------------------------------------------------------------

class RamCollection(GenCollection):

    db: RamDb
    name: str = ""
    documents: Dict[DocId, JsonDoc] = {}

    def __init__(self, db: RamDb, name: str):
        self.db = db
        self.name = name
        self.documents = {}

    def __str__(self):
        """ return the collection's state """
        r = form("<%s>:\n", self.name)
        r += json.dumps(self.documents, sort_keys=True, indent=4)
        return r


    def count(self, q: QuerySpec=None) -> int:
        """ returns the number of documents that matched the spec
        For now, return count of all documents.
        """
        if q is None:
            return len(self.documents)
        else:
            co = 0
            for d in self.documents.values():
                if queries.matchesQuery(d, q):
                    co += 1
            #//for d
            return co

    def find(self,
             q: QuerySpec=None,
             skip: int=0,
             limit: int=0,
             sort: SortSpec=None)\
        -> Iterator[JsonDoc]:
        """ return documents matching a spec
        """
        queries.assertValidQuery(q)
        skipped = 0
        emitted = 0
        for id, j in sorting.sortDocs(self.documents, sort):
            if not queries.matchesQuery(j, q):
                continue
            if skipped<skip:
                skipped += 1
                continue
            if limit>0 and emitted>=limit:
                return # no more docs

            emitted += 1
            yield addId(j, id)
        #//for

    def find_one(self,
                 q: QuerySpec=None,
                 skip: int=0,
                 sort: SortSpec=None)\
        -> Optional[JsonDoc]:
        """ find a document """

    def delete_one(self, id: DocId):
        """ delete a document based on its id """
        self.documents.pop(id, None)

    def delete_many(self,
                    q: QuerySpec=None):
        """ delete all documents that match a specification """


    def getDoc(self, id: DocId) -> Optional[JsonDoc]:
        """ returns the document with the id, or None if it
        doesn't exist. """
        if id in self.documents:
            return addId(self.documents[id], id)
        else:
            return None


    def insert_one(self, jDoc: JsonDoc):
        """ save a document, where the document has an id.
        It might be a new document or over-write an existing one """
        if "_id" in jDoc and isinstance(jDoc['_id'], DocId):
            id = jDoc["_id"]
        else:
            id = self.makeNewId()
        self.documents[id] = removeId(jDoc)

    def makeNewId(self) -> DocId:
        """ make a new id for the new document """
        return self.name + "-" + self.db.makeIdStub()


#end
