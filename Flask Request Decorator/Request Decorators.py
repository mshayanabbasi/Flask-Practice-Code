from flask import Flask

app = Flask(__name__)

request_state = ''

@app.before_request
def before_request():
    global request_state
    request_state += ' before'
@app.after_request
def after_request(resp):
    global request_state
    request_state += ' after'
    return resp
@app.teardown_request
def teardown_request(execp):
    global request_state
    request_state += ' teardown <br>'
    return execp
@app.route('/')
def index():
    return 'Hello ' + request_state


app.run(debug=True ,  port=4040)
