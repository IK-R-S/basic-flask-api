import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Bem vindo ao exemplo básico de API com Flask!</h1>
    <p>Nesse exemplo você pode explorar as seguintes rotas, algumas delas com parâmetros:</p>
    <li><a href="/olamundo">Olá mundo no flask 🌎</a></li>
    <li><a href="/boasvindas/">Boas vindas dinâmico 😃</a></li>
    <li><a href="/soma/">Soma de 2 números 🔢</a></li>
    <li><a href="/jsoncalc/">Resposta em JSON 📃</a></li>
    <text style="margin-top: 10">by: @IK.R.S</text>
    """


@app.route("/olamundo/")
def hello():
    return "Olá mundo"

@app.route("/boasvindas/")
def boasvindas():
    return "Escreva seu nome no endereço. exemplo: http://127.0.0.1:4444/boasvindas/Maria"

@app.route("/boasvindas/<nome>")
def bemvindo(nome):
    return f"Olá {nome}, seja bem vindo a API Flask!"

@app.route("/soma/")
def sum():
    return """
    <h2>Para somar escreva os números no endereço da seguinte forma: http://127.0.0.1:4444/soma/1/2</h3>
    
    <p1>Neste exemplo os número foram 1 e 2; veja com 3 e 4: http://127.0.0.1:222/soma/3/4</p1>
    """


@app.route("/soma/<n1>/<n2>")
def sumnum(n1, n2):
    sum = int(n1) + int(n2)
    return f"SOMA ENTRE {n1} E {n2} = {sum}"

@app.route("/jsoncalc/")
def jsoncalc():
    return """
    <h2>Para receber os dados em JSON escreva os números no endereço da seguinte forma: http://127.0.0.1:4444/jsoncalc/1/2</h3>
    
    <p1>Neste exemplo os número foram 1 e 2; veja com 3 e 4: http://127.0.0.1:222/jsoncalc/3/4</p1>
    """

@app.route("/jsoncalc/<n1>/<n2>")
def calc(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    soma = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    div = n1 / n2
    return jsonify({"soma": soma, "subtracao": sub, "multiplicacao": mult, "divisao": div})

app.run(port="4444", debug=False)
