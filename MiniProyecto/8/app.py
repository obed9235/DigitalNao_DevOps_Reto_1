from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu', methods=['POST'])
def menu():
    option = request.form.get('option')
    response = ''

    if option == '1':
        response = 'Has seleccionado la opción 1: Ver saldo.'
    elif option == '2':
        response = 'Has seleccionado la opción 2: Recargar saldo.'
    else:
        response = 'Opción no válida.'

    return render_template('response.html', response=response)

if __name__ == '__main__':
    app.run()
