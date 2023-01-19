# test_all.py = perform all tests

from quickiebase import lintest

group = lintest.TestGroup()

import test_butil
group.add(test_butil.group)

import test_queries
group.add(test_queries.group)

import test_sorting
group.add(test_sorting.group)

import test_ramdb
group.add(test_ramdb.group)

import test_dbmdb
group.add(test_dbmdb.group)


if __name__=='__main__': group.run()


#end
