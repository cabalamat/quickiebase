# About <i class="fas fa-shipping-fast"></i> Quickiebase

Quickiebase (abbreviated **QB**) is (or rather, will be, once it's done) a pure-Python NoSQL database with a similar API to MongoDB.

## Why Quickiebase?

Python is renowned for being batteries-included. It also has access to sqlite as part of the standard library. I think it would make sense to have an NoSQL document database as part of the standard library; something that can you can set up and start using with a simple `import` statement.

(If not as part of the standsrd library, then it should be available as a package on the [Python Package Index](https://pypi.org/).)

According to the [2022 Stack Overflow developer survey](https://survey.stackoverflow.co/2022/#technology-most-popular-technologies), MongoDB is the most popular NoSQL database (and the 4th most popular database overall), and the  most wanted NoSQL database which 17% of developers wanting to use it.

Because of this, the NoSQL database library should be based on MongoDB, that is its functionality should be a subset of MongoDB's, so that if a project using it grows to something big it can easily move up to a bigger database.  

I'm also mindful that MongoDB stopped being open source with its Server Side Public License (SSPL).

## Quickiebase roadmap

Quickiebase will be [developed in stages](roadmap).

## Icon for Quickiebase

This Font Awesome icon: <i class="fas fa-shipping-fast"></i>

Of possibly a [running man](https://thenounproject.com/icon/speed-7358642/) from Noun Project:

![](speed.png)

## See also

* [[Roadmap]] of how Quickiebase will be developed
* [Program documentation](program_documentation) documents the internals of the QB program (as opposed to its external interface), including
    * [[dbmdb module]]
* [[Similar projects]]
* [[dbviewer]] is a command line tool for inspecting Quickiebase databases
* documentation for [MongoDB's pymongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/)
* [Pymongo API documentation](https://pymongo.readthedocs.io/en/stable/api/index.html)
