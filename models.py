from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

# Criando uma classe base para a declaração das tabelas
Base = declarative_base()

# Primeiro modelo para a tabela
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)
    
    def __repr__(self):
        return "<User(name={}, fullname={}, age={})>".format(self.name, self.fullname, self.age, self.id)
