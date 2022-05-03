from produto import Produto
from dao import ProdutoDao
from flask import Flask, render_template, request, url_for, redirect, flash, session

produto_dao = ProdutoDao('banco_dados.db')

app = Flask(__name__)
app.secret_key = 'softgraf'


@app.route('/')
def index():
    lista = produto_dao.listar()
    return render_template('relatorio.html', titulo='relatório de estoque', produtos=lista)


@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    return render_template('cadastrar.html', titulo='Cadastra Novo Produto')


@app.route('/salvar', methods=['post'])
def salvar():
    id = request.form['id']
    descricao = request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    produto = Produto(descricao, preco, quantidade, id)
    produto_dao.salvar(produto)
    return redirect(url_for('index'))


@app.route('/deletar/<string:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    produto_dao.deletar(id)
    flash('O produto foi removido com sucesso!')
    return redirect(url_for('index'))


@app.route('/editar/<string:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    produto = produto_dao.buscar_por_id(id)
    flash('O produto foi editado com sucesso!')
    return render_template('editar.html', titulo='Editar Produto', produto=produto)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Desconectado com sucesso')
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['senha'] == '123456789':
        #salva o usuário logado
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect(url_for('index'))
    else:
        flash('Senha inválida! Tente novamente')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)
    #app.run(debug=True, host='0.0.0.0')