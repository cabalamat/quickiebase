# sorting.py = sorting documents

"""
Sorting allows you to determine which order documents are returned
from a find().

"""

from typing import List, Union, Dict, Optional, Any, Tuple
import functools

from .butil import *
from .quickietypes import DocId, JsonDoc, IdDictJsonDoc, IdJsonDoc

#---------------------------------------------------------------------



""" a specification for sorting """
SortSpecItem = Union[str, Tuple[str,int]]
SortSpec = Union[None, SortSpecItem, List[SortSpecItem]]
NormalisedSortSpec = List[Tuple[str,int]]

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
    if sortArg is None: return []
    if isinstance(sortArg, (str,tuple)):
        sortArg = [sortArg]
    newSortArg = [term if isinstance(term, tuple)
                       else (term, 1)
                  for term in sortArg]
    return newSortArg


#---------------------------------------------------------------------

def getTypeInt(x) -> int:
    """ return an int for a type """
    if isinstance(x, type(None)): return 1

    # must test for bool before int because a bool is an int
    if isinstance(x, bool): return 6

    if isinstance(x, (int, float)): return 2
    if isinstance(x, str): return 3
    if isinstance(x, dict): return 4
    if isinstance(x, list): return 5

    #anything else:
    return 7


def sortDocs(docDict: IdDictJsonDoc,
             sort: SortSpec
    ) -> List[IdJsonDoc]:
    """
    Given a dict of documents, sort them according to the sort criteria
    in (sort).

    Local variable names:
    fn:str = field name
    d:int = direction, 1 for ascending, -1 for decending
    idDoc:Tuple[DocId,JsonDoc]  = a document
    """
    nss: NormalisedSortSpec = normaliseSort(sort)

    # if not sorting on _id, add it as a tie-breaker
    if not any(fn=="_id" for fn,d in nss):
        nss.append(("_id",1))

    def sortCmpFunction(idDoc1, idDoc2) -> int:
        for fn, d in nss:
            if fn=="_id":
                fv1 = idDoc1[0]
                fv2 = idDoc2[0]
            else:
                fv1 = idDoc1[1].get(fn, None)
                fv2 = idDoc2[1].get(fn, None)
            ft1 = getTypeInt(fv1)
            ft2 = getTypeInt(fv2)

            # different types?
            if ft1<ft2: return -d
            if ft1>ft2: return d

            #>>>> must be same type
            if ft1==1:
                pass # None is always equal to None
            elif ft1 in (4,5,7):
                # compare reprs
                rv1 = repr(fv1)
                rv2 = repr(fv2)
                if rv1<rv2: return -d
                if rv1>rv2: return d
            else:
                if fv1<fv2: return -d
                if fv1>fv2: return d
        #//for
        return 0

    docIdList = kv(docDict)
    result = sorted(docIdList, key=functools.cmp_to_key(sortCmpFunction))
    return result



#---------------------------------------------------------------------


#end

