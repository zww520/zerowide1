from flask import Flask
from flask import render_template

app = Flask('zerowide')

@app.route('/')
def index():
    return render_template('index.html')
def run():
    app.run()


