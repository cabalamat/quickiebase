# pages.py = pages of webviwer

from flask import request, redirect, Response

import allpages
from allpages import *

#---------------------------------------------------------------------

@app.route("/")
def frontPage():
    return "This is Webviewer!"

#---------------------------------------------------------------------




#end
