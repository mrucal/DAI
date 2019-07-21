# -*- coding: utf-8 -*-

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')                       
def index():
   return '''
   <html>
		<body>
			<svg width="600" height="600">
              <line x1="{0}" x2="{1}" y1="{2}" y2="{3}" stroke="yellow" stroke-width="4" />
              <rect x="{4}" y="{5}" height="{6}" width="{7}" stroke="yellow" stroke-width="4" />
              <ellipse cx="{8}" cy="{9}" rx="{10}" ry="{11}" stroke="yellow" stroke-width="4"  />
            </svg>
		</body>
	</html>'''.format(random.randint(0, 600),random.randint(0, 600),random.randint(0, 600),random.randint(0, 600),
		random.randint(0, 600),random.randint(0, 600),random.randint(0, 600),random.randint(0, 600),
		random.randint(0, 600),random.randint(0, 600),random.randint(0, 600),random.randint(0, 600))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)