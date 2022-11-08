from sqlite3 import Time
from tkinter.tix import CheckList
from flask import Flask, render_template
from datetime import datetime
import json


app = Flask(__name__)
now = datetime.now()

@app.route ('/')
def api():
    return render_template('modelo.json')
    
# tempo

@app.route('/etapa')
def tiempo():
   return render_template('etapa.json')

    for i in ()
    timestamp = 0
    date_time = datetime.fromtimestamp(timestamp)

    d = date_time.strftime("%c")
    print("Output 1:", d)	

    d = date_time.strftime("%x")
    print("Output 2:", d)

    d = date_time.strftime("%X")
    print("Output 3:", d)
    


    
    
