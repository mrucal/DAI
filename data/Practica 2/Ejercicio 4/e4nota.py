# -*- coding: utf-8 -*-
#127.0.0.1:8080/mandelbrot?x1=-1&y1=-1&x2=1&y2=.1&a=300&p=0,0,255;255,0,0;0,255,0&it=16

from flask import Flask,request
import mandelbrot
import os
import time

app = Flask(__name__)

def elimina_antiguos(ficheros):

	for fichero in ficheros:
		# Hora actual - hora del fichero (convertido a horas)
		if (time.time()-os.stat('static/cache/'+fichero)[-1])/3600 >= 24:
			os.remove('static/cache/'+fichero)

@app.route('/mandelbrot')
def mensaje():

	# Obtener argumentos del GET
	x1 = request.args.get('x1')
	y1 = request.args.get('y1')
	x2 = request.args.get('x2')
	y2 = request.args.get('y2')
	a = request.args.get('a')
	p = request.args.get('p',default = '0,0,255;255,0,0;0,255,0')
	it = request.args.get('it', default = '16')

	# Construir la cadena con el nombre de la imagen
	fichero = '&'.join([x1,y1,x2,y2,a,p,it])+'.png'
	# Obtener las imagenes que hay en la carpeta cache
	ficheros = os.listdir(path='./static/cache/')

	elimina_antiguos(ficheros)
	
	res="La imagen estaba en la cache."
	# Si no hay una imagen con los parametros obtenidos se crea
	if fichero not in ficheros:
		res="Creando imagen..."
		# Convertir la cadena p a lista
		p=[tuple([int(j) for j in i.split(',')]) for i in p.split(';')]
		# Crear la imagen
		mandelbrot.renderizaMandelbrotBonito(float(x1), float(y1),float(x2), float(x2), int(a), 100, './static/cache/'+fichero, p, int(it))

	

	return '''
   <html>
		<body>
			<p>{1}</p>
			<img src="{0}" />
		</body>
	</html>'''.format('static/cache/'+fichero,res)

if __name__ == '__main__':
    app.run(host='0	.0.0.0', debug = True)