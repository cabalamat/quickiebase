# dbviewer.py = quick database viewer


import argparse
from pathlib import Path
import dbm

from quickiebase import butil
from quickiebase.butil import *

from quickiebase.quickietypes import *
from quickiebase import dbmdb
from quickiebase.dbmdb import DbmDb, DbmCollection

DEFAULT_BASE_DIR = "~/.local/share/dbmdb/"

def listDatabases():
    """ list databases that exist """
    dbmDbBase = Path(DEFAULT_BASE_DIR).expanduser()
    #print(f"{dbmDbBase=}")
    #print(f"{dbmDbBase.is_absolute()}")

    #>>>>>
    subdirs = list(dbmDbBase.iterdir())
    #print(f"{subdirs=}")
    if len(subdirs)==1:
        isAre = "is"
        s = ""
    else:
        isAre = "are"
        s = "s"
    print(f"There {isAre} {len(subdirs)} database{s}:")
    for db in subdirs:
        print(f"   {db.name}")

    #//for

def dbInfo(dbName: str):
    """ output info for a database """

    print(f"===== database: {dbName} =====")
    base = Path(DEFAULT_BASE_DIR).expanduser()
    dbP = base / dbName

    #print(f"{dbP=} is_abnsolute? {dbP.is_absolute()}")
    collections = list(dbP.iterdir())
    print(f"There are {len(collections)} collections:")
    for col in collections:
        print(f"   {col.name}")
    #//for

    for col in collections:
        colInfo(dbName, col.name)
    #//for

def colInfo(dbName: str, colName: str):
    print(f"----- database: {dbName} col: {colName} -----")
    colPath = Path(DEFAULT_BASE_DIR).expanduser() / dbName / colName
    #print(f"{colPath=} is_abnsolute? {colPath.is_absolute()}")

    db = dbm.open(colPath)
    for key in sorted(db.keys()):
        val = db[key]
        #print(f"{key}: {val}")
        ks = key.decode(encoding="utf-8")
        vs = val.decode(encoding="utf-8")
        print(f"{ks}: {vs}")
    #//for

#---------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description=
        "*** Quickiebase Database Viewer ***")

    parser.add_argument("-v", "--verbose", action="count",
        help="increase output verbosity")
    parser.add_argument("-l", "--list", action='store_true',
        help="list databases")
    parser.add_argument("-d", "--db", type=str, metavar="DBNAME",
        help="output info for a database")


    args = parser.parse_args()
    if args.list:
        listDatabases()
    if args.db:
        dbInfo(args.db)
    else:
        prn("Hint: use -h to get help information")



if __name__=='__main__':
    main()

#end
