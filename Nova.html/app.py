from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@app.route('/resultado')
def resultado():
    # Pega os valores enviados pelo formulário via GET
    try:
        numero1 = float(request.args.get('numero1', 0))
        numero2 = float(request.args.get('numero2', 0))
    except ValueError:
        numero1 = 0
        numero2 = 0
        
    operacao = request.args.get('operacao')
    
    resultado_conta = 0
    nome_operacao = ""

    # Lógica da calculadora
    if operacao == '+':
        resultado_conta = numero1 + numero2
        nome_operacao = "Adição"
    elif operacao == '-':
        resultado_conta = numero1 - numero2
        nome_operacao = "Subtração"
    elif operacao == '*':
        resultado_conta = numero1 * numero2
        nome_operacao = "Multiplicação"
    elif operacao == '/':
        if numero2 == 0:
            resultado_conta = "Erro"
            nome_operacao = "Divisão por zero"
        else:
            resultado_conta = numero1 / numero2
            nome_operacao = "Divisão"

    # Formata para remover o ".0" caso seja um número inteiro
    if isinstance(resultado_conta, float) and resultado_conta.is_integer():
        resultado_conta = int(resultado_conta)
    if isinstance(numero1, float) and numero1.is_integer():
        numero1 = int(numero1)
    if isinstance(numero2, float) and numero2.is_integer():
        numero2 = int(numero2)

    return render_template('resultado.html', 
                           numero1=numero1, 
                           operacao=operacao, 
                           numero2=numero2, 
                           resultado=resultado_conta, 
                           nome_operacao=nome_operacao)

if __name__ == '__main__':
    app.run(debug=False)
