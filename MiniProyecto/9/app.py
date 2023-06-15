from flask import Flask, render_template

app = Flask(__name__)

movies = [
    {
        'title': 'Origen',
        'rating': '8.0'
    },
    {
        'title': 'Interstellar',
        'rating': '7.9'
    },
    {
        'title': 'Avatar',
        'rating': '7.2'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ratings')
def ratings():
    return render_template('ratings.html', movies=movies)

if __name__ == '__main__':
    app.run()
