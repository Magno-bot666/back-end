from flask import Blueprint, render_template


usuario_bp = Blueprint('user',__name__ )



@usuario_bp.route('/login')
def login():
    return render_template('login.html')

@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
