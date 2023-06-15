from flask import Flask, render_template, request

app = Flask(__name__)

def number_to_words(number):
    # Diccionario de palabras para los números del 0 al 19
    num_dict = {
        0: 'cero',
        1: 'uno',
        2: 'dos',
        3: 'tres',
        4: 'cuatro',
        5: 'cinco',
        6: 'seis',
        7: 'siete',
        8: 'ocho',
        9: 'nueve',
        10: 'diez',
        11: 'once',
        12: 'doce',
        13: 'trece',
        14: 'catorce',
        15: 'quince',
        16: 'dieciséis',
        17: 'diecisiete',
        18: 'dieciocho',
        19: 'diecinueve'
    }

    # Diccionario de palabras para las decenas
    tens_dict = {
        2: 'veinte',
        3: 'treinta',
        4: 'cuarenta',
        5: 'cincuenta',
        6: 'sesenta',
        7: 'setenta',
        8: 'ochenta',
        9: 'noventa'
    }

    if number < 20:
        return num_dict[number]
    elif number < 100:
        tens = number // 10
        units = number % 10
        if units == 0:
            return tens_dict[tens]
        else:
            return tens_dict[tens] + ' y ' + num_dict[units]
    else:
        return 'Número fuera de rango'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = int(request.form['number'])
        words = number_to_words(number)
        return render_template('index.html', words=words)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
