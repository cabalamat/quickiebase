# test_all.py = perform all tests

from quickiebase import lintest

group = lintest.TestGroup()

import test_queries
group.add(test_queries.group)

import test_ramdb
group.add(test_ramdb.group)


if __name__=='__main__': group.run()


#end
