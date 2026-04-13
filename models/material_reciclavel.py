from sqlalchemy import Column, String, Integer, Float

from  models.base import Base

class MaterialReciclavel(Base):
    __tablename__ = 'material_reciclavel'

    codigo = Column(Integer, primary_key=True)
    categoria = Column(String(20), nullable=False)
    quantidade_kg = Column(Float, default=0.0)
    valor_kg = Column(Float, nullable=False)

    def __init__(self, codigo:int, quantidade_kg: float, categoria:str, valor_kg:float):
        """Construtor da classe MaterialReciclavel"""
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade_kg = quantidade_kg if quantidade_kg else 0.0   
        self.valor_kg = valor_kg
    
    def atualizar_quantidade(self, quantidade_kg: float):
        """Atualiza a quantidade de material reciclável disponível"""
        self.quantidade_kg += quantidade_kg
    