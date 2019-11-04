from bottle import route, run

@route('/hello')
def hello():
    return "Hello from outside sad?!"

run(host='0.0.0.0', port=5002, debug=True)