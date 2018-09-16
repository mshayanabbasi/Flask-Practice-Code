from flask import Flask, json, jsonify, request

app=Flask(__name__)


languages = [{'name':'JavaScript'}, {'name':'Python'}, {'name':'Ruby'}, {'name':'C++'}]

@app.route('/', methods=['GET'])
def index():
    return jsonify({'languages':'It works'})

@app.route('/lang', methods=['GET'])
def get_all():
    return jsonify({'languages':languages})
@app.route('/lang/<string:name>', methods=['GET'])
def get_one(name):
    langs = [language for language in languages if language['name']== name]
    return jsonify({'languages': langs[0]})
if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=4000)
