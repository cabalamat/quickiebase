# dbmdb module

The `dbmdb.py` module implements these classes:

* `DbmDb` = a database
* `DbmCollection` = a collection in a database

## DbmCollection

Important instance variables are:

```py
    documents: Dict[DocId, JsonDoc] = {}
    inRam: bool = False # documents currently in RAM?
    ud = None # underlying dbm database
```

`documents` holds its documents (this is inhrited from `RamCollection`)