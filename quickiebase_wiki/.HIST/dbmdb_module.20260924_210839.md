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

`documents` holds the collection's documents (this is inherited from `ramdb.RamCollection`)

`ud` is a pointer to the underlying dbm database. It is initialised by:

```py 
        self.pan = butil.join(db.dbDir, name)
        self.ud = dbm.open(self.pan, 'c')
```

`inRam` says whether the contents of the database are in ram (in the `documents` instance vartiable) or not. When the database is initialised, 
they are not. If the database has to do an operation that includes reading them all, such as `find()`, then all the database is read into
ram before the operation is performed.

Once the database is `inRam`, it can be read without reading the database on disk. Note that whenerver the database is modified
it must be modified on disk, and if `inRam` is true the ram-copy of the database is also altered.

In any case the disk-copy of the database remains the single source of truth.