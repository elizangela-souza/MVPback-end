from pydantic import BaseModel, Field
from typing import List, Optional
from models.cliente import Cliente

class ClienteSchema(BaseModel):
    cnpj: str = Field(..., example="20182807000442")
    nome: str  = Field(..., example="Empresa Recicladora")
    cep: str = Field(..., examples="72221064")
    logradouro: Optional[str] = Field(None, examples="Rua 25 sul")
    bairro: Optional[str] = Field(None, examples="Taguatinga")
    cidade: Optional[str] = Field(None, examples="Brasília")
    uf: Optional[str] = Field(None, examples="DF")
    email: str = Field(..., example="email@gmail.com")
    telefone: Optional[str] = Field(None, example="(61)99999-9999")

def visualizar_cliente(cliente: Cliente):
    return {
        "cnpj": cliente.cnpj,
        "nome": cliente.nome,
        "cep": cliente.cep,
        "logradouro": cliente.logradouro,
        "bairro": cliente.bairro,
        "cidade": cliente.cidade,
        "uf": cliente.uf,
        "email": cliente.email,
        "telefone": cliente.telefone
    }

class ListaClientesSchema(BaseModel):
    clientes: list[ClienteSchema]

def listar_clientes(clientes: List[Cliente]) -> List[Cliente]:
     return [ClienteSchema(
        cnpj= cliente.cnpj,
        nome=cliente.nome,
        cep=cliene.cep,
        email=cliente.email,
        telefone=cliente.telefone
    ) for cliente in clientes]

class ConsultaClienteSchema(BaseModel):
    cnpj: str 

class AtualizarClienteSchema(BaseModel):
    cnpj: str
    nome: Optional[str] = None
    cep: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None

class ExclusaoClienteSchema(BaseModel):
    cnpj: str 

class ExcluirClienteSchema(BaseModel):
    mesage: str
    cnpj: str
