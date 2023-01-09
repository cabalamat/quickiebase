# dbmdb.py = Database implemented on dbm


from typing import List, Tuple, Union, Dict, Optional, Any, Iterator

from . import butil
from .butil import form

from .quickietypes import DocId, JsonDoc

from .gendb import GenDb, GenCollection
from .ramdb import RamDb, RamCollection

#---------------------------------------------------------------------

class DbmDb(GenDb):
    """ a local database, in RAM """

#---------------------------------------------------------------------

class DbmCollection(RamCollection):


#---------------------------------------------------------------------

#end
