import pygal
import json
from urllib2 import urlopen  
from flask import Flask, render_template,request
from pygal.style import DarkSolarizedStyle
 
app = Flask(__name__)
@app.route('/',methods=('GET','POST'))
def get_execution_time():
    if request.method == 'POST':
        line_chart = pygal.Line()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002,2013))
        line_chart.add('NSS', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
        line_chart.add('KMP', [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        line_chart.add('LCSS',[85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('BM',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        line_chart.render()
    return render_template('graph.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)
