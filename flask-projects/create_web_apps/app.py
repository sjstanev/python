from flask import Flask, render_template, request, redirect, url_for


# initialize flask
app = Flask(__name__)

@app.route('/index')
def index():
    return 'Python Flask'

# dynamic page using templates using variables
# @app.route("/user/<a>/<b>")
# to pass multiple variables to a templates, pass a dictonary
# context = {'a':a, 'b':b, 'c':c }
# render_template('index.html', **context')
# Inside the template use {{a}}, {{b}} or iterate over the dictionary
@app.route('/success/<bmi>')
def success(bmi):
    # return f'Your BMI is {bmi}'
    elements = [1, 2, 4, 6, 8]
    return render_template('bmi.html', bmi = bmi, elements = elements)

@app.route('/scripts/')
def scripts():
    return render_template('index.html')

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        height = request.form['height']
        height = float(height)
        mass = request.form['mass']
        mass =float(mass)
        bmi = mass / (height*height)
        bmi = round(bmi, 2)
        return redirect(url_for('success', bmi = bmi))
    else:
        return render_template('home.html')


app.run(host = '0.0.0.0', port=5000)