from .import bp as auth
from .forms import LoginForm, RegisterForm, EditProfileForm
from flask import flash, request, redirect, url_for, render_template
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required



@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        email = request.form.get('email').lower()
        password = request.form.get('password')
        u = User.query.filter_by(email=email).first()
        if u and u.check_hashed_password(password):
            login_user(u)
            flash('Welcome back!', 'success')
            return redirect(url_for('main.index'))
        flash('Incorrect Email/Password Combo', 'danger')
        return render_template('login.html.j2', form = form)
    return render_template('login.html.j2', form = form)


@auth.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have logged out, see you soon!', 'warning')
        return redirect(url_for('auth.login'))


@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method=='POST' and form.validate_on_submit():
        try:
            new_user_data={
                'first_name': form.first_name.data.title(),
                'last_name': form.last_name.data.title(),
                'email': form.email.data.lower(),
                'password': form.password.data,
                'icon': form.icon.data
            }
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
            new_user_object.save()
        except:
            flash('There was an unexpected Error creating your account. Please try again.', 'danger')
            return render_template('register.html.j2', form = form)
        flash("You have successfully registered! Let's login and catch some Pokemon!", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html.j2', form = form)



@auth.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if request.method=='POST' and form.validate_on_submit():
        new_user_data ={
            'first_name': form.first_name.data.title(),
            'last_name': form.last_name.data.title(),
            'email': form.email.data.lower(),
            'password': form.password.data,
            'icon': form.icon.data if form.icon.data !="a0" else current_user.icon
        }
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and user.email != current_user.email:
            flash('Email already in use! Please input another')
            return redirect(url_for('auth.edit_profile'))
        try:
            current_user.from_dict(new_user_data)
            current_user.save()
            flash('Your profile was successfully updated!', 'success')
        except:
            flash('There was an unexpected error. Please try again!', 'danger')
            return redirect(url_for('auth.edit_profile'))
        return redirect(url_for('main.index'))
    return render_template('register.html.j2', form=form)


