from flask import Flask, jsonify
app = Flask(__name__)
import actions
import glob

@app.route('/overview/')
def get_overview():
    mods = [i[8:-3] for i in glob.glob("actions/*.py")]
    values = []
    for i in mods:
        func = getattr(__import__("actions.%s" % i), i, None).get_value
        values.append({"value": func(), "format_string": func.__doc__})
    return jsonify(value=values)

@app.route('/<action>/')
def get_status(action):
    value = getattr(__import__("actions.%s" % action), action, None).get_value
    return jsonify(value=value(), format_string=value.__doc__)

app.run(host='0.0.0.0')
