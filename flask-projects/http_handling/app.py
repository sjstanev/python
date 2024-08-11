from flask import Flask, render_template, request, redirect, url_for
# import python script that you want to itterate
import switches

app = Flask(__name__)

@app.route('/')
def register():

    return render_template('register.html')

@app.route('/login', methods = ['POST'])
def login():
    form = request.form
    # print html form result to console
    print(form)
    # call the function from swithcs module
    returned_array = switches.loop_array()
    return render_template('login.html', form = form, returned_array = returned_array)

app.run(host = '0.0.0.0', port=3000)