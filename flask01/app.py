from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola mundo!'

@app.route('/adios')
def adios_mundo():
    return 'Adios mundo!'

@app.route('/hola')
def hola_html():
    return '<h1>Hola tu!</h1>'

@app.route('/json')
def json():
    return Response( '{"nombre":"john"}', mimetype='application/json' )

@app.route('/xml')
def xml():
    xml = '<?xml version="1.0"?>' \
    '<nombre>john</nombre>'
    return Response(xml, mimetype='application/xml')

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)