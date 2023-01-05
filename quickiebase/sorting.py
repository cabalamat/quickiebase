# sorting.py = sorting documents

"""
Sorting allows you to determine which order documents are returned
from a find().

"""

from typing import List, Union, Dict, Optional, Any, Tuple

from .quickietypes import DocId, JsonDoc

#---------------------------------------------------------------------



""" a specification for sorting """
SortSpecItem = Union[str, Tuple[str,int]]
SortSpec = Union[None, SortSpecItem, List[SortSpecItem]]
NormalisedSortSpec = Union[None, List[Tuple[str,int]]]

def normaliseSort(sortArg: SortSpec) -> NormalisedSortSpec:
    """ Normalise sort argument.
    This puts the sort argument into a form that pymongo requires. See:
    <http://api.mongodb.org/
    python/current/api/pymongo/cursor.html#pymongo.cursor.Cursor.sort>
    Examples:

    'foo' -> [('foo', 1)]
    ('bar',-1) -> [('bar', -1)]
    [('foo',-1), 'bar'] -> [('foo', -1), ('bar', 1)]

    @return = the sort argument in the way that pymongo requires it
    """
    if sortArg is None: return None
    if isinstance(sortArg, (str,tuple)):
        sortArg = [sortArg]
    newSortArg = [term if isinstance(term, tuple)
                       else (term, 1)
                  for term in sortArg]
    return newSortArg


#---------------------------------------------------------------------

def sortDocs(docDict: Dict[DocId, JsonDoc],
               sort: SortSpec
    ) -> List[Tuple[DocId,JsonDoc]]:
    """
    Given a dict of documents, sort them according to the sort criteria
    in (sort).
    """

#---------------------------------------------------------------------


#end

