from sqlalchemy import Column, String

from models.base import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    cnpj = Column(String(14), primary_key=True)
    nome = Column(String(120), nullable=False)
    cep = Column(String(8), nullable=False)
    logradouro = Column(String(50), nullable=True)
    bairro = Column(String(50), nullable=True)
    cidade = Column(String(50), nullable=True)
    uf = Column(String(2), nullable=True)
    email = Column(String(30), nullable=True)
    telefone = Column(String(14), nullable=False)

    def __init__(self, cnpj: str,  nome: str, cep:str, logradouro:str, bairro:str, cidade:str, uf:str, email:str, telefone: str):
        """Construtor da classe Cliente"""
            
        self.cnpj = cnpj
        self.nome = nome
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.email = email
        self.telefone = telefone