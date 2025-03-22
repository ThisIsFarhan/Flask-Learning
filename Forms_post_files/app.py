from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "Farhan" and password == "123":
            return "Login Success"
        else:
            return "Login Failed"
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()

@app.route('/handle_post',methods=['POST'])
def handle_post():
    greetings = request.json['greeting']
    name = request.json['name']

    with open('file.txt','w') as f:
        f.write(f"{greetings}, {name}")

    return jsonify({'message':"Data saved successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)