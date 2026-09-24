# Sorting

QB's `find()` method allows the order in which documents are returned to be defined. E.g., if `employee` is a table of employees, then:

```py
employee.find(sort=[('location',1), ('age',-1)])
```

Returns employees by increasing location, and within that location by decreasing age.

When a comparison operator's operands are the same type (e.g. both numbers) it's obvious how to sort them. But what if they are different types, for example, one is a string and the other a number? Then they must be sorted based on their type.

## MongoDB collation order

Sorting disparate types in MongoDB is called *type bracketing*. The following order is used (lowest to highest):

* MinKey (internal type)
* Null
* Numbers (ints, longs, doubles, decimals)
* Symbol, String
* Object
* Array
* BinData
* ObjectId
* Boolean
* Date
* Timestamp
* Regular Expression
* MaxKey (internal type)

(from [Comparison/Sort Order](https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/))

## CouchDB collation order

from [3.2.2.5. Collation Specification](https://docs.couchdb.org/en/3.2.2-docs/ddocs/views/collation.html):

```
// special values sort before all other types
null
false
true

// then numbers
1
2
3.0
4

// then text, case sensitive
"a"
"A"
"aa"
"b"
"B"
"ba"
"bb"

// then arrays. compared element by element until different.
// Longer arrays sort after their prefixes
["a"]
["b"]
["b","c"]
["b","c", "a"]
["b","d"]
["b","d", "e"]

// then object, compares each key value in the list until different.
// larger objects sort after their subset objects.
{a:1}
{a:2}
{b:1}
{b:2}
{b:2, a:1} // Member order does matter for collation.
           // CouchDB preserves member order
           // but doesn't require that clients will.
           // this test might fail if used with a js engine
           // that doesn't preserve order
{b:2, c:2}
```

## Python collation order

Python doesn't collate different types:

```py
>>> sorted([2,3,5,1,"hello",None])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
```

So looks like I'll have to write my own comparison function!


