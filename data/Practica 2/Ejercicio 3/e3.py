# -*- coding: utf-8 -*-

from flask import Flask,request
app = Flask(__name__)

@app.route('/user/<username>')
def hola_user(username):
	res = 'Hola %s!!' % username
	if username == 'Pepe':
		res = 'Bienvenido Pepe!!'
	return res

@app.route('/mensaje')
def mensaje():
	texto = request.args.get('texto')
	return texto
 
@app.errorhandler(404)
def page_not_found(error):
	return 'Página no encontrada!!!', 404

if __name__ == '__main__':
    app.run(host='0	.0.0.0', debug = True)