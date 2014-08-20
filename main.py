#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/<search>" ,methods=['GET' , 'POST'])
def network(search):

    if search == "search":
        code_input=request.form['codeinput']
        combo_list=request.form['thelist']
        message=combo_list

    templateData = {
        'message' : message
    }
    return render_template('index.html',**templateData)

if __name__ == "__main__":
    app.run(host='172.16.51.28', port=80, debug=True)
