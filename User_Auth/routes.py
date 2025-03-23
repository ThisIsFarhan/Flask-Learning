from flask import render_template, request, redirect, url_for
from models import User
from flask_login import login_user, logout_user, current_user, login_required

def register_routes(app, db, bcrypt):
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup',methods=['GET','POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            usrname = request.form.get('username')
            password = request.form.get('password')

            hashed_pass = bcrypt.generate_password_hash(password)

            user = User(username = usrname, password = hashed_pass)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

    @app.route('/login',methods=['GET','POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            usrname = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username == usrname).first()
            
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return "Failed to login"
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/somepage')
    @login_required
    def somepage():
        return "Page Data"