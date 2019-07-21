# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')                         # decorador, varia los parametros
def hello_world():                      # I/O de la función
   return '''
   <html>
		<head>
			<title>Hello wolrd</title>
			<link href="./static/style.css" rel="stylesheet" type="text/css" />
		</head>

		<body>
			<p>Hola mundo!!</p>
			<img src="static/Lenna.png" />
		</body>
	</html>'''
if __name__ == '__main__':
    app.run(host='0	.0.0.0', debug = True)