from models.conexao import *

class Pedido(Base):
 __tablename__ = "pedido"
 id = Column("id", Integer, primary_key=True, autoincrement=True)
 cliente = Column("cliente", String(200))
 pecas = Column("pecas", String(200))
 estado = Column("estado", String(200))
 preco = Column("preco", String(20))
 email = Column("email", String(50))
 
 def __init__(self, cliente, pecas, estado, preco, email):
    self.cliente = cliente
    self.pecas = pecas
    self.estado = estado
    self.preco = preco
    self.email = email
    
# Criando as tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)
