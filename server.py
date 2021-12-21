# https://flask.palletsprojects.com/en/1.1.x/quickstart/
import random

from flask import Flask
app = Flask(__name__)
num = random.randrange(10)

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/TFHSQWDrJQzwRuLZGU/giphy.gif" width="480" height="480"></img>'

@app.route('/<number>')
def check(number):
    number = int(number)
    if number > num:
        return '<h1 style="color:black">Number is too high!</h1>'\
               '<img src="https://media.giphy.com/media/JT7Td5xRqkvHQvTdEu/giphy.gif" width="480" height="480"></img>'
    elif number < num:
        return '<h1 style="color:red">Number is too low!</h1>' \
               '<img src="https://media.giphy.com/media/ZyVUHyoYN9i2q8xAQP/giphy.gif" width="480" height="480"></img>'
    else:
        return '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/ZWd5Xu4osF8k6M5iLJ/giphy.gif" width="480" height="480"></img>'

if __name__ == "__main__":
    app.run(debug=True)
