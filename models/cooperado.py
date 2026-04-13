from sqlalchemy import Column, String, DateTime

from models.base import Base

class Cooperado(Base):
    __tablename__ = 'cooperado'

    matricula = Column(String(6), primary_key=True)
    nome = Column(String(120), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    data_nascimento = Column(DateTime, nullable=False)
    telefone = Column(String(14), nullable=True)

    def __init__(self, matricula: str,  nome: str, cpf:str, data_nascimento: DateTime, telefone: str):
        """Construtor da classe Cooperado"""
            
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone