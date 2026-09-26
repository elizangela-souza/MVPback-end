from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from models.base import Base

class RegistroVenda(Base):
    __tablename__ = 'registro_venda'

    
    id_registro = Column(Integer, primary_key=True, autoincrement=True)

    #Relacionamento com a tabela Cliente e com a tabela Material
    id_cliente = Column(String(6), ForeignKey('cliente.cnpj'), index=True, nullable=False)
    id_material = Column(Integer, ForeignKey('material_reciclavel.codigo'), index=True, nullable=False)

    data_venda = Column(DateTime, default=datetime.now(), index=True)
    kg_material = Column(Float, nullable=False)
    valor_venda = Column(Float, nullable=True)
     
    # Relacionamento com MaterialReciclavel para acessar valor_kg
    material_reciclavel = relationship('MaterialReciclavel')