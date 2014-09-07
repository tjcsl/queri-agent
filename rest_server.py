from flask import Flask, jsonify
app = Flask(__name__)
import actions
import glob
import json
import os
import os.path
import shutil
import stat
import time
import uuid

config = json.load(open("config.json"))
def update_index():
    retval = []
    for directory in config["directories"]:
        print(directory)
        for k in os.listdir(directory):
            print(k)
            retval.append(("%s/%s" % (directory, k), os.stat("%s/%s" % (directory, k))[stat.ST_MTIME]))
    return retval
global index
index = update_index()

def filename_score(one, two):
    three = two.split()
    five = 0
    six = 7200
    for four in three:
        if four in one:
            five += six
    return five

def do_heuristic(index, search):
    index = [(i, j - time.time() + filename_score(i, search)) for i, j in index]
    print(index)
    return [a[0] for a in sorted(index, key=lambda k: -k[1])]

def do_copy_file(x):
    ext = ""
    if x.count(".") > 0:
        ext = x.split(".")[-1]
    dest = str(uuid.uuid4()) + "." + ext
    shutil.copy(x, "static/%s" % dest)
    return "/static/%s" % dest

@app.route('/overview/')
def get_overview():
    mods = [i[8:-3] for i in glob.glob("actions/*.py") if "__init__" not in i]
    values = []
    for i in mods:
        func = getattr(__import__("actions.%s" % i), i, None).get_value
        values.append({"value": func(), "format_string": func.__doc__})
    return jsonify(value=values)

@app.route("/matchfile/<thing>/")
def matchfile(thing):
    global index
    index = update_index()
    matches = do_heuristic(index, thing)
    ourmatches = []
    for i in matches[:10]:
        ourmatches.append(do_copy_file(i))
    return jsonify(matches=ourmatches)

@app.route('/<action>/')
def get_status(action):
    value = getattr(__import__("actions.%s" % action), action, None).get_value
    return jsonify(value=value(), format_string=value.__doc__)

app.run(host='0.0.0.0', debug=True)
