from flask import Flask, render_template, request
from birthday_generator import BirthdayWishGenerator

app = Flask(__name__)
generator = BirthdayWishGenerator()

@app.route('/', methods=['GET', 'POST'])
def home():
    wish = None
    if request.method == 'POST':
        # name = request.form.get('name', 'Friend')
        wish = generator.generate_wish()
    return render_template('birthday.html', wish=wish)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
