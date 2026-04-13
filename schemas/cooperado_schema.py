from datetime import datetime

from pydantic import BaseModel, Field
from typing import List, Optional
from models.cooperado import Cooperado

class CooperadoSchema(BaseModel):
    matricula: str 
    nome: str = Field(..., example="Maria Santos")
    cpf: str  = Field(..., example="01234567891")
    data_nascimento: datetime = Field(..., example="1970-03-29")
    telefone: Optional[str] = Field(None, example="(61)99999-9999")

def visualizar_cooperado(cooperado: Cooperado):
    return {
        "matricula": cooperado.matricula,
        "nome": cooperado.nome,
        "cpf": cooperado.cpf,
        "data_nascimento": cooperado.data_nascimento,
        "telefone": cooperado.telefone
    }

class ListaCooperadosSchema(BaseModel):
    cooperados: list[CooperadoSchema]

def listar_cooperados(cooperados: List[Cooperado]) -> List[Cooperado]:
     return [CooperadoSchema(
        matricula=cooperado.matricula,
        nome=cooperado.nome,
        cpf=cooperado.cpf,
        data_nascimento=cooperado.data_nascimento,
        telefone=cooperado.telefone
    ) for cooperado in cooperados]

class ConsultaCooperadoSchema(BaseModel):
    matricula: str 

class AtualizarCooperadoSchema(BaseModel):
    matricula: str
    nome: Optional[str] = None
    telefone: Optional[str] = None

class ExclusaoCooperadoSchema(BaseModel):
    id: str 

class ExcluirCooperadoSchema(BaseModel):
    mesage: str
    matricula: str

   

