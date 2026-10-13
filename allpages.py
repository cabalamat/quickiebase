# allpages.py = (for webviwer) stuff relevant to all pages

import os.path
import collections
import html
import datetime
import inspect
import sys

from flask import Flask, request
app = Flask(__name__)
#app.config["SECRET_KEY"] = "don't tell anyone" # not using
app.config["SESSION_COOKIE_NAME"] = "session_7489"
app.config["WERKZEUG_DEBUG_PIN"] = "off"

from quickiebase import butil

#---------------------------------------------------------------------
# jinja2 environment

import jinja2
from jinja2 import Template

jinjaEnv = jinja2.Environment()
thisDir = os.path.dirname(os.path.realpath(__file__))
templateDir = butil.join(thisDir, "templates")
jinjaEnv.loader = jinja2.FileSystemLoader(templateDir)


#---------------------------------------------------------------------
# debugging

def prt(formatStr="", *args):
    """ For debugging -- print a message, prepended with timestamp, function,
    line number.
    Uses old-style '%' format strings.
    @param formatStr::str
    @param args::[]
    """
    now = datetime.datetime.now()
    nowStr = now.strftime("%H:%M:%S.%f")
    caller = inspect.stack()[1]
    fileLine = caller[2]
    functionName = caller[3]
    s = butil.form(formatStr, args)
    t = "%s %s():%d: " % (nowStr, functionName, fileLine)
    sys.stderr.write(t + s + "\n")

#---------------------------------------------------------------------


#end
