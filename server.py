import flask
import json
from flask import request
import os
import sys


app = flask.Flask('phonebook')


@app.route('/', methods=['get'])
def home():
    files = os.listdir('%s/data' % sys.path[0])
    return flask.Response(json.dumps(files), mimetype='application/json')


@app.route('/<filename>', methods=['get'])
def fetch(filename):
    try:
        fullpath = '%s/data/%s' % (sys.path[0], filename)
        with open(fullpath, 'r') as json_file:
            data = json.load(json_file)
        return flask.Response(json.dumps(data), mimetype='application/json')
    except Exception as oops:
        return str(oops), 500


@app.route('/new/<filename>', methods=['post'])
def post_new(filename):
    if '.json' not in filename:
        return 'Not a JSON filename', 500
    try:
        fullpath = '%s/data/%s' % (sys.path[0], filename)
        with open(fullpath, 'w') as json_file:
            json.dump(request.get_json(), json_file)
        return 'success', 200
    except Exception as oops:
        return str(oops), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
