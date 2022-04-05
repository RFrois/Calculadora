import os
from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
from math import sqrt

app  = Flask(__name__)

@app.route("/")
def main():
    return render_template('calc.html')

@app.route('/calc', methods=['GET', 'POST']) 
def calc():
    valor1 = request.form['v1']
    valor2 = request.form['v2']
    operacao = request.form['op']

    v1 = int(valor1)
    v2 = int(valor2)
    op = str(operacao)

    if (op == 'soma'):
        rc = (float(v1) + float(v2))
    elif (op == 'divisao'):
        rc = (float(v1) / float(v2))
    elif (op == 'subtracao'):
        rc = (float(v1) - float(v2))
    elif (op == 'multiplicacao'):
        rc = (float(v1) * float(v2))
    else:
        rc = 0
    return(str(rc))

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=8080)
