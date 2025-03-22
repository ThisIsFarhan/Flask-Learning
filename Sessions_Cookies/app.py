from flask import Flask, render_template, session, make_response, request

app = Flask(__name__, template_folder='templates')
app.secret_key = 'some key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_data')
def set_data():
    session["name"] = "Farhan"
    session["email"] = "blah@email.com"
    return render_template('index.html', message="Data set successfully")

@app.route('/get_data')
def get_data():
    if "name" not in session.keys() or "email" not in session.keys():
        return render_template('index.html', message="Session not found")
    name = session.get("name")
    email = session.get("email")
    return render_template('index.html', message=f"Name: {name}, Email: {email}")

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message="Session cleared")

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message="Cookie set successfully"))
    response.set_cookie("cookie_name", "cookie_value")
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_val = request.cookies.get("cookie_name")
    return render_template('index.html', message=f"Cookie Value: {cookie_val}")

@app.route('/clear_cookie')
def clear_cookie():
    response = make_response(render_template('index.html', message="Cookie cleared successfully"))
    response.set_cookie("cookie_name", expires=0)
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)