import os
from crypt import methods
from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
from math import sqrt
from CalculadoraBasica import CalculadoraBasica 

app  = Flask(__name__)

@app.route('/calc') 

def calc():
    if methods == "POST":
        valor1=request.form.get("v1")
        valor2=request.form.get("v2")
        operacao=request.form.get("op")

        v1 = int(valor1)
        v2 = int(valor2)
        op = str(operacao)

        rc = CalculadoraBasica()

        if (op == "soma"):
            rc = (float(v1) + float(v2))
        elif (op == "divisao"):
            rc = (float(v1) / float(v2))
        elif (op == "subtracao"):
            rc = (float(v1) - float(v2))
        elif (op == "multiplicacao"):
            rc = (float(v1) * float(v2))
        else:
            print("errouuuu")
        return(rc)
    #calc()
if __name__ == ("__main__"):
    app.run(host='0.0.0.0', port=80)
