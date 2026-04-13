from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models.base import Base

class RegistroTriagem(Base):
    __tablename__ = 'registro_triagem'

    
    id_registro = Column(Integer, primary_key=True, autoincrement=True)

    #Relacionamento com a tabela Cooperado e com a tabela Material
    id_cooperado = Column(String(6), ForeignKey('cooperado.matricula'), index=True, nullable=False)
    id_material = Column(Integer, ForeignKey('material_reciclavel.codigo'), index=True, nullable=False)

    data_triagem = Column(DateTime, default=datetime.now(), index=True)
    kg_material = Column(Float, nullable=False)
     
    # Relacionamento com MaterialReciclavel para acessar valor_kg
    material_reciclavel = relationship('MaterialReciclavel')