from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo! Mi primer app de Flask, yupi'
@app.route('/Elsa')
def elsa():
    return 'Hola, estas en la página Elsa'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
