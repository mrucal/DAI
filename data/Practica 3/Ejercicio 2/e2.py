# -*- coding: utf-8 -*-

from flask import Flask, render_template, session
from flask import request, redirect, url_for

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


def login_history():

	e1,e2,e3 = construye_enlaces(len(history))

	if len(history) <= 1:
		return render_template('index_login.html', name = session['username'])
	if len(history) == 2:
		return render_template('index_login.html', name = session['username'], e1 = e1, n1 = history_name[-2])
	if len(history) == 3:
		return render_template('index_login.html', name = session['username'], e1 = e1, e2 = e2, n1 = history_name[-2], n2 = history_name[-3])
	if len(history) >= 4:
		return render_template('index_login.html', name = session['username'], e1 = e1, e2 = e2, e3 = e3, n1 = history_name[-2], n2 = history_name[-3], n3 = history_name[-4])

def append_historial( history_act, history_name_act):

	history.append(history_act)
	session['history'] = history
	history_name.append(history_name_act)
	session['history_name'] = history_name

	return session

@app.route('/', methods=['GET', 'POST'])                       
def index():

	session = append_historial('/', 'Index')
	
	if 'username' in session:
		return login_history()

	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		history.clear()
		history_name.clear()
		session = append_historial('/', 'Index')
		session['username'] = request.form['username']
		return login_history()

	return render_template('index_no_login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():

	session = append_historial('/logout', 'Logout')
	session.pop('history', None)
	session.pop('history_name', None)
	session.pop('username', None)
	history.clear()
	history_name.clear()

	return redirect(url_for('index'))

@app.route('/enlace')
def enlace():

	enlace = request.args.get('e')
	nombre = request.args.get('nombre')

	session = append_historial(enlace, nombre)

	return redirect(enlace)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	history = []
	history_name = []
	app.run(host='0 .0.0.0', debug = True)