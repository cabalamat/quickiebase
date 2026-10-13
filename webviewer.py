# webviewer.py = web based interface for Quickiebase

import argparse

from flask import request, redirect

import allpages
from allpages import *

# pages:
import pages

# default port
DEFAULT_PORT = 7489

#---------------------------------------------------------------------

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""\
vewviewer: a web-based viewer for Quickiebase
""")
    parser.add_argument("-d", "--debug",
        help="Run in debugging mode",
        action="store_true")
    parser.add_argument("-p", "--port",
        help="Port number to use",
        type=int,
        default=DEFAULT_PORT)
    parser.add_argument("-v", "--verbose",
        help="Make output more verbose",
        action="store_true")
    commandLineArgs = parser.parse_args()
    print(f"{commandLineArgs=}")
    host = "127.0.0.1" if commandLineArgs.debug else "0.0.0.0"

    app.run(host=host,
        port=commandLineArgs.port,
        debug=commandLineArgs.debug)



#end
