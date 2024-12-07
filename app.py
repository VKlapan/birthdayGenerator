from flask import Flask, render_template, request, session
from birthday_generator import BirthdayWishGenerator

app = Flask(__name__)
app.secret_key = 'aP3xW9lmNpOQ2uL5V1'
generator = BirthdayWishGenerator()

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'counter' not in session:
        session['counter'] = 1
    header, body1, body2 = None, None, None
    if request.method == 'POST':
        header, body1, body2 = generator.generate_wish()
        session['counter'] += 1
    return render_template('birthday.html', header=header, body1=body1, body2=body2, counter = session['counter'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
