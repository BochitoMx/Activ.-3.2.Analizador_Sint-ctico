from flask import Flask, render_template, request
from lexer import analizar_codigo
from parser import parse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_lexico = []
    resultado_sintactico = []

    if request.method == 'POST':
        codigo = request.form['codigo']
        
        resultado_lexico = analizar_codigo(codigo)

        resultado_sintactico = parse(codigo)

    return render_template('index.html', resultado_lexico=resultado_lexico, resultado_sintactico=resultado_sintactico)

if __name__ == '__main__':
    app.run(debug=True)
