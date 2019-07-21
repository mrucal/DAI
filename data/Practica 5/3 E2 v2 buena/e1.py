# -*- coding: utf-8 -*-

from flask import Flask, render_template, session
from flask import request, redirect, url_for
import shelve
from pymongo import MongoClient
from flask import jsonify

app = Flask(__name__)


# ----------------------------- PRACTICAS 2 Y 3 ------------------------------------------------------------------------------

def construye_enlaces(ne):

	e1 = ''
	e2 = ''
	e3 = ''

	if ne >= 4:
		e3 = '/enlace?e='+history[-4]+'&nombre='+history_name[-4]
	if ne >=3:
		e2 = '/enlace?e='+history[-3]+'&nombre='+history_name[-3]
	if ne >= 2:
		e1 = '/enlace?e='+history[-2]+'&nombre='+history_name[-2]

	return e1,e2,e3

def get_history():
	
	e1,e2,e3 = construye_enlaces(len(history))

	if len(history) <= 1:
		return {}
	if len(history) == 2:
		return {'n1': history_name[-2],'e1':e1}
	if len(history) == 3:
		return {'n1': history_name[-2],'e1':e1,'n2': history_name[-3],'e2':e2}
	if len(history) == 5:
		del history[0]
		del history_name[0]
	return {'n1': history_name[-2],'e1':e1,'n2': history_name[-3],'e2':e2,'n3': history_name[-4],'e3':e3}


def append_historial( history_act, history_name_act):

	history.append(history_act)
	session['history'] = history
	history_name.append(history_name_act)
	session['history_name'] = history_name



@app.route('/', methods=['GET', 'POST'])                       
def index():

	
	
	if 'loginCORRECTO' in session:
		append_historial('/', 'Index')

		h = get_history()
		return render_template('index_login.html',username = session['username'],h = h)

	return render_template('index_no_login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		db = shelve.open('usuarios/db_usuarios.db', writeback=True)
		history.clear()
		history_name.clear()
		append_historial('/login', 'Login')
		username = request.form['username']
		password = request.form['password']
		if username in db:
			if db[username]['password'] == password:
				session['loginCORRECTO'] = 'loginCORRECTO'
				session['username'] = username
				db.close()
				return redirect(url_for('index'))
			else:
				db.close()
				return render_template('formulario_login.html', mensaje_error = 'La contraseña es incorrecta.')
		else:
			db.close()
			return render_template('formulario_login.html', mensaje_error = 'El usuario no esta en la base de datos.')
	return render_template('formulario_login.html')
		
@app.route('/logout', methods=['GET', 'POST'])
def logout():

	append_historial('/logout', 'Logout')
	session.pop('history', None)
	session.pop('editando', None)
	session.pop('history_name', None)
	session.pop('username', None)
	session.pop('loginCORRECTO',None)
	history.clear()
	history_name.clear()

	return redirect(url_for('index'))

@app.route('/registro', methods=['GET', 'POST'])
def registro():
	if 'editando' in session:
		h = get_history()
		return render_template('registro.html',username = session['username'], h = h, nombre = session['editando'][0], email = session['editando'][1], user = session['editando'][2],editar=True)
	else:
		return render_template('registro.html')

@app.route('/confirmarregistro', methods=['GET', 'POST'])
def confirmarregistro():

	if request.method == 'POST':

		db = shelve.open('usuarios/db_usuarios.db', writeback=True)
		
		username = request.form['username']

		mensaje_error=''

		h = get_history()

		if username == '':
			mensaje_error = 'El campo usuario no puede estar vacío.'

		nombre = request.form['nombre']
		if nombre == '':
			mensaje_error = 'El campo nombre no puede estar vacío.'

		email = request.form['email']

		password = request.form['password']
		if password == '':
			mensaje_error = 'El campo password no puede estar vacío.'

		
		if username not in db or 'editando' in session:
			session.pop('editando', None)
			db[username] = {'nombre': nombre, 'email': email, 'password': password}
			session['loginCORRECTO'] = 'loginCORRECTO'
			session['username'] = username
		else:
			mensaje_error = 'El usuario ya existe.'

		if 'editando' in session:
			nombre_edit = session['editando'][0]
			email_edit = session['editando'][1]
			user_edit = session['editando'][2]
			editar = True
		else:
			nombre_edit = ''
			email_edit = ''
			user_edit = ''
			editar = ''
		name = user_edit

		if mensaje_error != '':
			return render_template('registro.html', username=name, h = h, mensaje_error=mensaje_error, nombre= nombre_edit, email = email_edit, user = user_edit, editar = editar)

	return redirect(url_for('index'))

@app.route('/enlace')
def enlace():

	enlace = request.args.get('e')
	nombre = request.args.get('nombre')

	append_historial(enlace, nombre)

	return redirect(enlace)

@app.route('/<user>',methods=['GET'])
def perfil(user):

	append_historial('/' + user, 'Ver')

	db = shelve.open('usuarios/db_usuarios.db', writeback=True)

	nombre = db[user]['nombre']
	email = db[user]['email']

	db.close()

	h = get_history()
	return render_template('perfil.html', username = session['username'], h = h, nombre = nombre, email = email)

@app.route('/editar/<user>',methods=['GET'])
def editar_perfil(user):

	append_historial('/editar/' + user, 'Editar')

	db = shelve.open('usuarios/db_usuarios.db', writeback=True)

	nombre = db[user]['nombre']
	email = db[user]['email']

	session['editando'] = (nombre, email, user)

	db.close()

	return redirect(url_for('registro'))

@app.route('/restaurantes',methods=['GET', 'POST'])
def restaurante():

	tb = request.args.get('tb')
	if tb == 'cocina':
		campo = 'cuisine'
	if tb == 'Barrio':
		campo = 'borough'
	if tb == 'Distrito':
		campo = 'address.zipcode'

	if request.method == 'POST':
		opcion = request.form['opcion']

		print(opcion)

		client = MongoClient()

		db = client.test

		
		opciones=obtener_posibles_valores(campo)
		cursor = db.restaurantes.find({campo:opcion})

		encontrados = []
		for d in cursor:
			if d['name'] == "":
				d['name'] = "-"
			if tb == 'cocina':
				encontrados.append({'nombre':d['name'],'direccion':d['address']['street']+', '+d['address']['building']+', '+d['borough'] + ', '+ d['address']['zipcode']},)
			if tb == 'Barrio':
				encontrados.append({'nombre':d['name'],'direccion':d['address']['street']+', '+d['address']['building']+ ', '+ d['address']['zipcode'], 'cocina': d['cuisine']})
			if tb == 'Distrito':
				encontrados.append({'nombre':d['name'],'direccion':d['address']['street']+', '+d['address']['building']+', '+d['borough'], 'cocina': d['cuisine']})				
			
		encontrados = sorted(encontrados, key=lambda k: k['nombre']) 


		h = get_history()
		if tb == 'cocina':
			return jsonify([encontrados,opcion,'false'])
		else:
			return jsonify([encontrados,opcion,'true'])

	else:		

		append_historial('/restaurantes?tb='+tb, 'Restaurantes-'+tb)

		opciones=obtener_posibles_valores(campo)

		h = get_history()
		if tb == 'cocina':
			return render_template('restaurantes.html',username =  session['username'], h= h , opciones = opciones, tb = tb)
		else:
			return render_template('restaurantes.html',username =  session['username'], h= h , opciones = opciones, tb = tb, nococina=True)

def obtener_posibles_valores(nombre_campo):
	client = MongoClient()
	db = client.test
	cursor = db.restaurantes.find()
	campo = set()
	for document in cursor:
		if nombre_campo == 'address.zipcode':
			campo.add(document['address']['zipcode'])
		else:
			campo.add(document[nombre_campo])

	campo = list(campo)
	campo.sort()
	return campo

# ------------------------- FIN PRACTICAS 2 Y 3 ------------------------------------------------------------------------------

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	history = []
	history_name = []
	app.run(host='0.0.0.0', debug = True)
