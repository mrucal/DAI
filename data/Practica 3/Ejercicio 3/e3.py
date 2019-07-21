# -*- coding: utf-8 -*-

from flask import Flask, render_template, session
from flask import request, redirect, url_for
import shelve

app = Flask(__name__)

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


def login_history(pag,name =-1, nombre = '', email = '', user = '', editar= '', mensaje_error=''):
	if name == -1:
		name=session['username']
	e1,e2,e3 = construye_enlaces(len(history))
	if len(history) <= 1:
		return render_template(pag, name = name, nombre = nombre, email = email, user= user, editar=editar, mensaje_error=mensaje_error)
	if len(history) == 2:
		return render_template(pag, name = name, e1 = e1, n1 = history_name[-2], nombre = nombre, email = email, user= user, editar=editar, mensaje_error=mensaje_error)
	if len(history) == 3:
		return render_template(pag, name = name, e1 = e1, e2 = e2, n1 = history_name[-2], n2 = history_name[-3], nombre = nombre, email = email, user= user, editar=editar, mensaje_error=mensaje_error)
	if len(history) >= 4:
		return render_template(pag, name = name, e1 = e1, e2 = e2, e3 = e3, n1 = history_name[-2], n2 = history_name[-3], n3 = history_name[-4], nombre = nombre, email = email, user= user, editar=editar, mensaje_error=mensaje_error)

def append_historial( history_act, history_name_act):

	history.append(history_act)
	session['history'] = history
	history_name.append(history_name_act)
	session['history_name'] = history_name

	return session

@app.route('/', methods=['GET', 'POST'])                       
def index():

	session = append_historial('/', 'Index')
	
	if 'loginCORRECTO' in session:
		return login_history('index_login.html')

	return render_template('index_no_login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		db = shelve.open('usuarios/db_usuarios.db', writeback=True)
		history.clear()
		history_name.clear()
		session = append_historial('/', 'Index')
		username = request.form['username']
		password = request.form['password']
		if username in db:
			if db[username]['password'] == password:
				session['loginCORRECTO'] = 'loginCORRECTO'
				session['username'] = username
				return redirect(url_for('index'))
			else:
				return render_template('formulario_login.html', mensaje_error = 'La contraseña es incorrecta.')
		else:
			return render_template('formulario_login.html', mensaje_error = 'El usuario no esta en la base de datos.')
	return render_template('formulario_login.html')
		
@app.route('/logout', methods=['GET', 'POST'])
def logout():

	session = append_historial('/logout', 'Logout')
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
		return login_history('registro.html', nombre = session['editando'][0], email = session['editando'][1], user = session['editando'][2],editar=True)
	else:
		print("BREAK")
		return render_template('registro.html')

@app.route('/confirmarregistro', methods=['GET', 'POST'])
def confirmarregistro():

	if request.method == 'POST':
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
		db = shelve.open('usuarios/db_usuarios.db', writeback=True)
		name = user_edit
		username = request.form['username']
		if username == '':
			return login_history('registro.html', name=name, mensaje_error = 'El campo usuario no puede estar vacío.', nombre= nombre_edit, email = email_edit, user = user_edit, editar = editar)
		nombre = request.form['nombre']
		if nombre == '':
			return login_history('registro.html',name=name, mensaje_error = 'El campo nombre no puede estar vacío.', nombre= nombre_edit, email = email_edit, user = user_edit, editar = editar)
		email = request.form['email']
		password = request.form['password']
		if password == '':
			return login_history('registro.html', name=name,mensaje_error = 'El campo password no puede estar vacío.', nombre= nombre_edit, email = email_edit, user = user_edit, editar = editar)

		if username not in db or 'editando' in session:
			session.pop('editando', None)
			db[username] = {'nombre': nombre, 'email': email, 'password': password}
			session['loginCORRECTO'] = 'loginCORRECTO'
			session['username'] = username
		else:
			return login_history('registro.html', name=name,mensaje_error = 'El usuario ya existe.', nombre= nombre_edit, email = email_edit, user = user_edit, editar = editar)

	return redirect(url_for('index'))

@app.route('/enlace')
def enlace():

	enlace = request.args.get('e')
	nombre = request.args.get('nombre')

	session = append_historial(enlace, nombre)

	return redirect(enlace)

@app.route('/<user>',methods=['GET'])
def perfil(user):

	session = append_historial('/' + user, 'Ver')

	db = shelve.open('usuarios/db_usuarios.db', writeback=True)

	nombre = db[user]['nombre']
	email = db[user]['email']

	return login_history('perfil.html', nombre=nombre,  email=email)

@app.route('/editar/<user>',methods=['GET'])
def editar_perfil(user):

	session = append_historial('/editar/' + user, 'Editar')

	db = shelve.open('usuarios/db_usuarios.db', writeback=True)

	nombre = db[user]['nombre']
	email = db[user]['email']

	session['editando'] = (nombre, email, user)

	print(user)
	return redirect(url_for('registro'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	history = []
	history_name = []
	app.run(host='0 .0.0.0', debug = True)
