from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

#Routes and URL processors
# @app.route('/hello', methods=['GET','POST'])
# def hello():
#     if request.method == 'GET':
#         return "GET: Hello World"
#     elif request.method == 'POST':
#         return "POST: Hello World"

@app.route('/hello')
def hello():
    response = make_response('Hello world')
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {(num1) + (num2)}"

@app.route('/handle_url_params')
def handle_params():
    #requests.args returns a dictionary of the query string parameters
    # return str(request.args)
    if 'name' in request.args.keys():
        name = request.args['name']
        return "Hello! " + name
    else:
        return "Missing name parameter"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)