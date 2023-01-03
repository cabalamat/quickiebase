# Quickiebase roadmap

Quickiebase will be developed in stages. Here is the roadmap.


## Phase 1

In phase 1 Quickiebase will be a pure-Python library storing data in dbm (which is part of the Python standard library).
Each Quickiebase collection will be a separate dbm database, and within that dbm database, each record will be stored as 
JSON data in a separate record. The dbm key will be the Quickiebase `_id` for that record. 

### Querying the data

It's a priority of Quickiebase that its functionality will be a subset of MongoDB's. This is so that if the project becomes big, 
it will be easy to switch over to a MongoDB database. In particular Quickiebase will implement MongoDB's `find()` function, e.g.:

```py
employee.find({"location": "Glasgow", "age": {"$gt": 30}},
              skip = 20,
              limit = 20,
              sort = [("age", 1)])
```

This looks for employees in Glasgow aged >30, sorted by ascending age, skips the first 20, and returns at most 20 results.

There will also be other utility functions, e.g. to export a whole collection or database to an external json file:

```py
employee.exportToJson("myfile.json")
```

## Phase 2

Phase 2 extends Quickiebase by allowing the underlying database to be a separate one, such as a MongoDB or CouchDB database. Commands to Quickiebase are sent to the eternal database and the results put back to the calling Python program.

here we have:

```none
  /.................. one process ..............\     separate process
                                                      (possibly on 
                                                      separate server)

 ┌─────────────┐    ┌─────────────┐    ┌─────────┐    ┌─────────┐
 │ application │--->│ quickiebase │--->│ pymongo │===>│ MongoDB │
 │ program     │    │ library     │    │         │    │         │
 └─────────────┘    └─────────────┘    └─────────┘    └─────────┘             

or:

 ┌─────────────┐    ┌─────────────┐                   ┌─────────┐
 │ application │--->│ quickiebase │==================>│ CouchDB │
 │ program     │    │ library     │                   │         │
 └─────────────┘    └─────────────┘                   └─────────┘

```

Quickiebase talks to CouchDB using CouchDB's HTTP API.

## Phase 3

In phase 3 we build a standalone Quickiebase server. Since in Phase 2 we build a client that could talk the CouchDB API,
in phase 3 we'll build a server that acts as a CouchDB server. Thus, a Quickiebase client will be able to talk to a Quickiebase server.


