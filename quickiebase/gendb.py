# gendb.py = generic databases

"""
<gendb> is a generic interface to JSON document store databases.

"""

from typing import List, Union, Dict, Optional, Any, Tuple
from collections.abc import Iterator
from abc import ABC, abstractmethod
import secrets

from . import butil
from .butil import form

from .quickietypes import DocId, JsonDoc
from .sorting import SortSpec
from .queries import QuerySpec

#---------------------------------------------------------------------

class GenDb(ABC):
    """ a generic database """

    @abstractmethod
    def getCollection(self, colName: str) -> 'GenCollection':
        """ return a collection in this database, creating it if
        necessary
        """


#---------------------------------------------------------------------

class GenCollection(ABC):
    """ a generic collection/table """

    @abstractmethod
    def count(self,
              q: QuerySpec=None) -> int:
        """ returns the number of documents that matched the spec """

    @abstractmethod
    def find(self,
             q: QuerySpec=None,
             skip: int=0,
             limit: int=0,
             sort: SortSpec=None)\
        -> Iterator[JsonDoc]:
        """ return documents matching a spec
        """

    @abstractmethod
    def find_one(self,
                 query: QuerySpec=None,
                 skip: int=0,
                 sort: SortSpec=None)\
        -> Optional[JsonDoc]:
        """ find a document """

    @abstractmethod
    def delete_one(self, id: DocId):
        """ delete a document based on its id """

    @abstractmethod
    def delete_many(self,
                    q: QuerySpec=None):
        """ delete all documents that match a specification """

    @abstractmethod
    def getDoc(self, id: DocId) -> Optional[JsonDoc]:
        """ returns the document with the id, or None if it
        doesn't exist. """

    @abstractmethod
    def saveDoc(self, jDoc: JsonDoc):
        """ save a document.
        If the document has an id, then it over-writes and document with
        the same id in the collection.

        If the document doesn't have an id, it is given a unique one.
        """

    #==========

    def makeNewId(self, length:int=4) -> DocId:
        """ Create a new id for a new unused document in this
        collection.

        The id will be of length (length). If random ids of this length
        don't produce an unused id, the length is bumped up one.
        """
        ID_CHAR_SET = "0123456789abcdefghijklmnopqrstuvwxyz"
        tries = 0
        while True:
            candidateId = "".join(secrets.choice(ID_CHAR_SET)
                                  for i in range(0,length))
            doc = self.getDoc(candidateId)
            if doc is None:
                return candidateId
            tries += 1
            if tries >= 4:
                length += 1
                tries = 0
        #//while



#---------------------------------------------------------------------


#end
