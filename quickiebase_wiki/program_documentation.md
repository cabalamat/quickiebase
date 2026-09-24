# Program Documentation

QB includes the following source files:

* `queries.py` -- implements queries for the `find()` method
* `sorting.py` -- defines how documents are sorted by the `find()` method

Databases:

* `gendb.py` -- abstract classes saying what API a database must implement
* `ramdb.py` -- a database implemented in RAM (which therefore forgets everything when turned off)
* `dbmdb.py` -- a database implemnted in Python's dbm; see [[dbmdb module]] 
