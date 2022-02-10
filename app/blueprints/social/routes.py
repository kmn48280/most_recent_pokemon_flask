from .import bp as social
from flask import flash, redirect, url_for, render_template
from app.models import User, Pokemon, PokemonUser
from flask_login import login_required, current_user




@social.route('/show_users')
@login_required
def show_users():
    users = User.query.all()
    return render_template('show_users.html.j2', users=users)


@social.route('/battle', methods=['GET'])
@login_required
def battle():
    pass


