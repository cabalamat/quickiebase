# pages.py = pages of webviwer

from flask import request, redirect, Response

import allpages
from allpages import *

#---------------------------------------------------------------------

@app.route("/")
def front_page():
    tem = jinjaEnv.get_template("front_page.html")
    h = tem.render(
    )
    return h

#---------------------------------------------------------------------




#end
