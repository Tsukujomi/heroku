
import random

from flask import Flask, render_template, make_response, request


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    # random_number = request.cookies.get('random_number')
    if request.method == 'GET':
        response = make_response(render_template('index.html'))
        if not random_number:
            # response.set_cookie("random_number", str(random.choice(range(20))))
    else:
        guess = request.form.get('guess')
        if int(guess) == int(random_number):
            message = 'Teisingas spejimas!'
            response = make_response(
                render_template('index.html', message=message))
            # response.set_cookie(
            #     "random_number", str(random.choice(range(20))))

        elif int(guess) > int(random_number):
            message = 'Slaptas skaicius yra mazesnis'
            response = make_response(
                render_template('index.html', message=message))

        else:
            message = 'Slaptas skaicius yra didesnis'
            response = make_response(
                render_template('index.html', message=message))

    return response



if __name__ == '__main__':
    app.run(debug=True)
