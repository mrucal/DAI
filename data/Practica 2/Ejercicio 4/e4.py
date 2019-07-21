# -*- coding: utf-8 -*-
#127.0.0.1:8080/mandelbrot?x1=-1&y1=-1&x2=1&y2=.1&a=300 

from flask import Flask,request
import mandelbrot
app = Flask(__name__)

@app.route('/mandelbrot')
def mensaje():
	x1 = request.args.get('x1')
	y1 = request.args.get('y1')
	x2 = request.args.get('x2')
	y2 = request.args.get('y2')
	a = request.args.get('a')
	mandelbrot.renderizaMandelbrotBonito(float(x1), float(y1),float(x2), float(x2), int(a), 100, 'static/fractalWEB.png', [(0,0,255),(255,0,0),(0,255,0)], 16)
	return '''
   <html>
		<body>
			<img src="static/fractalWEB.png" />
		</body>
	</html>'''

if __name__ == '__main__':
    app.run(host='0	.0.0.0', debug = True)