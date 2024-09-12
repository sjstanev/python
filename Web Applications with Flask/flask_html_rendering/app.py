from lib2to3.fixes.fix_input import context

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():

    content = {"name": "Stanimir", "age": 30}
    return render_template('index.html', **content)

if __name__ == '__main__':
    app.run(debug=True)
    pass
