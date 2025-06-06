from flask import Blueprint, render_template


user_bp = Blueprint('user',__name__ )



@user_bp.route('/login')
def login():
    return render_template('login.html')

@user_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
