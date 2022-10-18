from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')