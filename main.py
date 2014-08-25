#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import sys
import os
import subprocess

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

        date_list = request.form['datelist']
        if date_list.rfind('-') - date_list.find('-') < 3:
            date_list = date_list[:date_list.find('-') + 1] + '0' + date_list[date_list.find('-') + 1:]
        if len(date_list) - date_list.rfind('-') < 3:
            date_list = date_list[:date_list.rfind('-') + 1] + '0' + date_list[date_list.rfind('-') + 1:]

        date_list= date_list.replace('-', '')

        proc = subprocess.Popen(['data/mini', 'data/' + date_list + '.csv', code_input], stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        message = out.split("\t")


    templateData = {
        'message' : message
    }
    return render_template('index.html',**templateData)

if __name__ == "__main__":
    app.run(host='172.16.51.28', port=8080, debug=True)
