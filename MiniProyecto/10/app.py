from flask import Flask, render_template, request

app = Flask(__name__)

secret_word = 'python'
max_attempts = 6
current_attempts = 0
guessed_letters = ['_'] * len(secret_word)

@app.route('/')
def home():
    return render_template('index.html', attempts=max_attempts, guessed_letters=' '.join(guessed_letters))

@app.route('/play', methods=['POST'])
def play():
    global current_attempts, guessed_letters
    letter = request.form.get('letter')

    if letter in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                guessed_letters[i] = letter

        if '_' not in guessed_letters:
            message = '¡Felicidades! sobreviviste!'
        else:
            message = '¡Letra correcta, te puedes salvar!'
    else:
        current_attempts += 1
        if current_attempts == max_attempts:
            message = '¡Estas Muerto!'
        else:
            message = 'Letra incorrecta puedes morir. ¡Intenta de nuevo!'

    return render_template('index.html', attempts=max_attempts - current_attempts, guessed_letters=' '.join(guessed_letters), message=message)

if __name__ == '__main__':
    app.run()
