from flask import Flask, render_template, request
app = Flask(__name__)

from models.usuario_model import *
from controllers.usuario_controller import *


if __name__ == '__main__':
    app.run(debug=True, port=5001)

@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/pecas')
def pecas():
    return render_template('pecas.html')

