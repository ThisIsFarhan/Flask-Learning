from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = "Farhan Ali Khan"
    result = 10 + 20
    list = [1,2,3,4,5,6,7,8,9,10]
    return render_template('index.html', value = myvalue, res = result, lst = list)

@app.route('/other_page')
def other():
    text = "This is a text"
    return render_template('other.html', txt=text)

@app.template_filter('reverse')
def reverse_string(string):
    return string[::-1]

@app.route('/redirect_page')
def redirect_page():
    return redirect(url_for('other'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)