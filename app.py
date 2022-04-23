from flask import Flask, jsonify, make_response
from flask_cors import CORS #, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '<p>Hello, world!</p>'

@app.route('/products')
# @cross_origin()
def products():
    produtos = [
            {
                'title': 'Caneca Personalizada de Porcelana',
                'amount': 45,
                'installments': { 'number': 3, 'total': 15, 'hasFee': True }
            },
            {
                'title': 'Caneca de Tulipa',
                'amount': 45,
                'installments': { 'number': 3, 'total': 15 },
            }
    ]
    response = make_response(jsonify(produtos))
    # response.headers.update({'Access-Control-Allow-Origin': '*'})
    response.headers.update({'Content-Type': 'application/json'})
    return response

app.run()
