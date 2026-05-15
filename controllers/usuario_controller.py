from main import app
from flask import request, render_template, redirect, session, url_for
from models.usuario_model import *

# Criando a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# rotas
@app.route("/usuario/novo")
def inserir():
 return render_template("usuario/usuario.html")

@app.route("/usuario/create", methods=['POST'])
def create():
 if request.method == 'POST':
 # Captura os dados enviados pelo formulário
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']

 # Cria um novo usuário
 new_user = Usuario(nome=nome, email=email,senha=senha,
telefone=telefone)

 # Cria um novo usuário no banco de dados
 db = SessionLocal()

 # Adiciona o novo usuário ao banco de dados
 db.add(new_user)
 db.commit()
 return redirect(url_for('lista'))

@app.route("/usuario/lista")
def lista():
    db = SessionLocal()
    # Consultar todos os usuários
    usuarios = db.query(Usuario).all()
    # Renderizar o HTML passando os dados
    return render_template('usuario/lista.html', usuarios=usuarios)

@app.route('/usuario/deletar/<int:item_id>')
def deletar(item_id):
    db = SessionLocal()
    item = db.query(Usuario).get(item_id) # Busca o item pelo id
    if item:
        db.delete(item) # Deleta o item
        db.commit()
    return redirect(url_for('lista'))

@app.route("/usuario/editar/<int:id>")
def editar(id):
    db = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    return render_template("usuario/atualizar.html", usuario=usuario)

@app.route("/usuario/editar", methods=["POST"])
def editar_usuario():
        db = SessionLocal()
        id = request.form.get("id")
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        telefone = request.form.get("telefone")

        usuario = db.query(Usuario).filter(Usuario.id == id).first()
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        usuario.telefone = telefone
        db.commit()
        return render_template("usuario/lista.html", usuarios=db.query(Usuario).all());


