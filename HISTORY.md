# HISTORY.md

History for Quickiebase. New entries go at end.

----

## 2023-Jan-09: created HISTORY.md

## 2023-Jan-09: started dbmdb.py

Next steps are to define allowed database/collection names (allow C
identifiers). Then allow databases/collections to be created, in the
standard directory (under `~/.local/share/dbmdb/`).

The stategy for collections will be that there will be a flag `inRam`.

When a collection is initialised by the program this will be `False`.
It will continue to be `False` until a method such as `find()` is performed,
at which point the whole collection is read into RAM (once) to do the
`find()` and any subsequent finds.

## 2023-Jan-15: more on dbmdb.DbmDb

## 2023-Jan-19:

* Passed 69 assertions in 22 test functions
* `wc *.py */*.py`: 2190 lines

## 2025-Nov-18

writing test suite that can be used by RamDb, DbmDb and other daybase classes.

## 2025-Nov-20

Created <test_suite.py>. Currently does not pass it. Saved to git.

/end/
