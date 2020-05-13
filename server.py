import flask
import json
from flask import request
import os
import sys


def rectify_filepath(filename):
    fullpath = '%s\data\%s' % (sys.path[0], filename)
    if not fullpath.endswith('.json'):
        fullpath = fullpath + '.json'
    return fullpath


def get_token_role(req):
    try:
        token = req.headers.get('token')
        fullpath = rectify_filepath('tokens.json')
        with open(fullpath, 'r') as json_file:
            tokens = json.load(json_file)
        for i in tokens:
            if i['token'] == token:
                return i['role']
        return None
    except:
        return None
    

app = flask.Flask('phonebook')



@app.route('/', methods=['get'])
def home():
    role = get_token_role(request)
    if role != 'readonly':
        return 'Token not accepted', 403
    files = os.listdir('%s/data' % sys.path[0])
    return flask.Response(json.dumps(files), mimetype='application/json')


@app.route('/<filename>', methods=['get'])
def fetch(filename):
    role = get_token_role(request)
    if role != 'readonly':
        return 'Token not accepted', 403
    try:
        fullpath = rectify_filepath(filename)
        with open(fullpath, 'r') as json_file:
            data = json.load(json_file)
        return flask.Response(json.dumps(data), mimetype='application/json')
    except Exception as oops:
        return str(oops), 500


@app.route('/new/<filename>', methods=['post'])
def post_new(filename):
    role = get_token_role(request)
    if role != 'readwrite':
        return 'Token not accepted', 403

    try:
        fullpath = rectify_filepath(filename)
        with open(fullpath, 'w') as json_file:
            json.dump(request.get_json(), json_file)
        return 'success', 201
    except Exception as oops:
        return str(oops), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context='adhoc')
