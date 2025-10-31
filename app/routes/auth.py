from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from .wtf import RegistrationForm
from app import db
from app.models import User
auth_bp = Blueprint('auth', __name__)
auth_bp.secret_key='make-for-register'
@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.name.data
        password=form.password.data
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'your account is created {username}')
        return redirect(url_for('auth.login'))

    return render_template("register.html", form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user'] = username
            flash('Login Successful!', 'success')
            return redirect(url_for('task.view_task'))
        else:
            flash("Invalid Credentials. Please try again.", 'error')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

        
