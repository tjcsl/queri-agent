from flask import Flask, jsonify
app = Flask(__name__)
import actions

@app.route('/<action>/')
def get_status(action):
    value = getattr(__import__("actions.%s" % action), action, None).get_value
    return jsonify(value=value(), format_string=value.__doc__)

app.run()
