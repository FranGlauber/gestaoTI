from models.conexao import *

class Pecas(Base):
 __tablename__ = "pecas"
 id = Column("id", Integer, primary_key=True, autoincrement=True)
 nome = Column("nome", String(200))
 login = Column("marca", String(200))
 senha = Column("estado", String(15))
 email = Column("cliente", String(100))
 
 def __init__(self, nome, marca, estado, cliente):
    self.nome = nome
    self.login = marca
    self.senha = estado
    self.email = cliente
    
# Criando as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)
