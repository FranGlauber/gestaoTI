from flask import Flask, render_template, request
from sqlalchemy import create_engine, Integer, String, Column, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:@localhost/loja')
Session = sessionmaker(bind=engine)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50),nullable=False)
    email = Column(String(100),nullable=False)
Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

@app.route('/usuarios/salvar', methods=['POST'])
def salvar_usuario():
    session=Session()
    nome = request.form.get('nome')
    email = request.form.get('email')

    usuarios=Usuario()
    usuarios.nome=nome
    usuarios.email=email
    
    session.add(usuarios)
    session.commit()

    return render_template('usuarios.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)