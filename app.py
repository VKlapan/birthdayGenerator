from flask import Flask, render_template, request
from birthday_generator import BirthdayWishGenerator

app = Flask(__name__)
generator = BirthdayWishGenerator()

@app.route('/', methods=['GET', 'POST'])
def home():
    header, body = None, None
    if request.method == 'POST':
        header, body = generator.generate_wish()
    return render_template('birthday.html', header=header, body=body)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
