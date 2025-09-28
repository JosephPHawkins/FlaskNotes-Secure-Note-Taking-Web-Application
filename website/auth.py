from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from .model import User 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password1').strip()

        user = User.query.filter_by(email=email).first()

        

        if user:
            
            if check_password_hash(user.password, password):
                flash(('Logged in successfully!'), category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again.', category='error')
        else:
            flash('email does not exist.', category='error')
    
    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email').strip()
        firstName = request.form.get('firstname')
        lastName = request.form.get('lastname')
        password1 = request.form.get('password1').strip()
        password2 = request.form.get('password2').strip()

        if User.query.filter_by(email=email).first():
            flash('email already exists.', category='error')
        elif len(email) < 4:
            flash('email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('first name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('passwords dont\'t match.', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 6 characters', category='error')
        else:
            flash('account created', category='success')
            
            hashed_password = generate_password_hash(password1, method="pbkdf2:sha256")
            new_user = User(email=email, first_name=firstName, last_name=lastName, password=hashed_password)
            
            from . import db
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            print(f"Stored password: {new_user.password!r}")
            return redirect(url_for('views.home'))
        
    return render_template('sign-up.html', user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    print("User logged out")
    return redirect(url_for('auth.login')) 

