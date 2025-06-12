from flask import Blueprint, render_template, request, redirect, url_for


usuario_bp = Blueprint('user',__name__ )



@usuario_bp.route('/login')
def login():
  
    return render_template('login.html')

    return render_template('login.html')

@usuario_bp.route('/acesso')
def acesso():
    
        username = request.form['login']
        password = request.form['senha']


        if username == "Magno" && password == username
        # Aqui você pode adicionar a lógica de autenticação
        print(f"{username}, {password}")
        return redirect (url_for('usuario.servicos'))
        

        print("usuario nao encontrado")
        return render_template('login.html')


@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
