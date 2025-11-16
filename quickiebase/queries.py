# queries.py

"""
Queries are criteria for determining wihch documents are returned
from a find().

E.g. if your documents are:

    {'name':'Caligula', 'age': 23}
    {'name':'Nero',     'age': 31}

And your query is:

    {'name':'Caligula'}

Then only the 1st document will be returned.

"""

from typing import List, Union, Dict, Optional, Any, Tuple

from . import butil
from .butil import form

from .quickietypes import *

#---------------------------------------------------------------------
# types

QuerySpec = Union[Dict, None]
""" a Mango-style query specification """

DictQuerySpec = Dict
""" a query spec that is a dict """


#---------------------------------------------------------------------
# does a document match a query?

def matchesQuery(jDoc: JsonDoc, q: QuerySpec) -> bool:
    """ does a document match query (q)? """
    if q is None or q=={}: return True
    return matchesDict(jDoc, q)

def matchesDict(jDoc: JsonDoc, q: DictQuerySpec) -> bool:
    """ a search where the query is a dict
    (and not $-forms)
    """
    for field, searchValue in butil.sortedKv(q):
        if field in jDoc:
            mf = matchesField(jDoc, field, searchValue)
            if not mf: return False
        else:
            # jDoc doesn't have that field, can't match
            return False
    #//for
    #all fields matched
    return True

def matchesField(jDoc: JsonDoc, field: str, searchValue) -> bool:
    """ This is a search on a field in (jDoc).
    It is a search like:
        {'name': 'Paul'}

    or:
        {'name': {'$gt': 'BBBB'}}

    or:
        {'name': {'$gt':  'BBBB',
                  '$lte': 'MMMM'}} # multiple comparisons
    """
    if not isinstance(searchValue, dict):
        # test for equality
        return jDoc[field] == searchValue

    return all(matchesOp(jDoc, field, op, value)
               for op, value in butil.sortedKv(searchValue))

def matchesOp(jDoc: JsonDoc, field: str, op: str, value) -> bool:
    """ This is a search of the form:
        {'name': {'$gt':  'BBBB',
                  '$lte': 'MMMM'}}
    at the $gt/$lte level, where:
    * field = "name"
    * op = "$gt"
    * value = "BBBB"

    operators include:
    $gt = greater than
    $gte = greater than or equal
    $lt = less than
    $lte = less than or equal
    $eq = equal
    $ne = not equal
    $in = in list of values
    $nin = not in list of values
    """
    #if op not in ["$gt","$gte","$lt","$lte","$eq","$ne"]:
    #    raise Exception(form("invalid operator %s", op))

    if op=="$gt": return jDoc[field] > value
    elif op=="$gte": return jDoc[field] >= value
    elif op=="$lt": return jDoc[field] < value
    elif op=="$lte": return jDoc[field] <= value
    elif op=="$eq": return jDoc[field] == value
    elif op=="$ne": return jDoc[field] != value
    elif op=="$in": return matchesIn(jDoc, field, value)
    elif op=="$nin": return matchesNin(jDoc, field, value)
    else:
        raise Exception(form("invalid operator '%s'", op))

def matchesIn(jDoc: JsonDoc, field: str, value) -> bool:
    """ search of the form:
    {'name': {'$in': ['foo', 'bar']}}
    where:
    * field = "name"
    * value = ['foo', 'bar']
    """
    if not isinstance(value, list):
        raise Exception(form("Argument to $in must be a list but is %r",
            value))
    return any(jDoc[field]==item for item in value)


def matchesNin(jDoc: JsonDoc, field: str, value) -> bool:
    """ $nin is the opposite of $in
    """
    if not isinstance(value, list):
        raise Exception(form("Argument to $nin must be a list but is %r",
            value))
    return not matchesIn(jDoc, field, value)


#---------------------------------------------------------------------
# query validity testing

"""
At the moment in `matchQuery()`, queries are tested for validitiy with
every document that they attempt to match,.

This is inefficient, so the `queryErrorMsg()` function attempts to do
it separately, so it can be run once for each search, not
again for each document.

(Currently unfinished)
"""

def assertValidQuery(q: QuerySpec):
    """ Raises an exception if query is invalid,
    else returns.
    This is a wrapper round queryErrorMsg().
    """
    msg = queryErrorMsg(q)
    if msg:
        raise Exception(form("Invalid searchSpec:\n    %r\n%s",
            q, msg))
    else:
        return

def queryErrorMsg(q: QuerySpec) -> str:
    """ Used to validate a query. if it is invalid,
    returns an appropriate error message.
    If it is valid, returns "".
    """
    if q is None or q=={}: return ""
    if not isinstance(q, dict):
        return form("query must be dict but is %r", q)
    return "" # no errors so valid



#---------------------------------------------------------------------

#end
