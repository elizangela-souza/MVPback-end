from datetime import datetime

from pydantic import BaseModel, Field
from typing import List
from models.registro_triagem import RegistroTriagem

class RegistroTriagemSchema(BaseModel):
    id_cooperado: str = Field(..., example="C12345")
    id_material: int = Field(..., example=200)
    data_triagem: datetime = Field(..., example="1970-03-29")
    kg_material: float = Field(..., example=3.0)


def visualizar_triagem(triagem: RegistroTriagem):
    return {
        "id_registro": triagem.id_registro,
        "id_cooperado": triagem.id_cooperado,
        "id_material": triagem.id_material,
        "data_triagem": triagem.data_triagem,
        "kg_material": triagem.kg_material
    }

class ListaTriagemSchema(BaseModel):
    materials: list[RegistroTriagemSchema]

def listar_triagens(triagens: List[RegistroTriagem]) -> List[RegistroTriagem]:
     return [RegistroTriagemSchema(
        id_registro = triagem.id_registro,
        id_cooperado = triagem.id_cooperado,
        id_material = triagem.id_material,
        data_triagem = triagem.data_triagem,
        kg_material = triagem.kg_material
    ) for triagem in triagens]

class ConsultaRegistroTriagemSchema(BaseModel):
    id_registro: int