# Home page for Quickiebase documentation

[TOC]

## Why Quickiebase?

Python is renowned for being batteries-included. It also has access to sqlite as part of the standard library. I think it would make sense to have an NoSQL document database as part of the standard library; something that can you can set up and start using with a simple `import` statement. (if not as part of the standrad library, then it should be available as a package on the [Python Package Index](https://pypi.org/).

According to the [2022 Stack Overflow developer survey](https://survey.stackoverflow.co/2022/#technology-most-popular-technologies), MongoDB is the most popular NoSQL database (and the 4th most popular database overall), and the  most wanted NoSQL database which 17% of developers wanting to use it.

Because of this, the NoSQL database library should be based on MongoDB, that is its functionality should be a subset of MongoDB's, so that if a project using it grows to something big it can easily move up to a bigger database.  

I'm also mindful that MongoDB stopped being open source with its Server Side Public License (SSPL).

## Quickiebase roadmap

Quickiebase will be [developed in stages](roadmap).