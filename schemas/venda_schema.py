from datetime import datetime

from pydantic import BaseModel, Field
from typing import List, Optional
from models.registro_venda import RegistroVenda

class RegistroVendaSchema(BaseModel):
    id_cliente: str = Field(..., example="20182807000442")
    id_material: int = Field(..., example=200)
    data_venda: datetime = Field(..., example="1970-03-29")
    kg_material: float = Field(..., example=3.0)
    valor_venda: Optional[float] = Field(None, example=200.0)


def visualizar_venda(venda: RegistroVenda):
    return {
        "id_registro": venda.id_registro,
        "id_cliente": venda.id_cliente,
        "id_material": venda.id_material,
        "data_venda": venda.data_venda,
        "kg_material": venda.kg_material,
        "valor_venda": venda.valor_venda
    }

class ListaVendaSchema(BaseModel):
    vendas: list[RegistroVendaSchema]

def listar_vendas(vendas: List[RegistroVenda]) -> List[RegistroVenda]:
     return [RegistroVendaSchema(
        id_registro = venda.id_registro,
        id_cliente = venda.id_cliente,
        id_material = venda.id_material,
        data_venda = venda.data_venda,
        kg_material = venda.kg_material,
        valor_venda = venda.valor_venda
    ) for venda in vendas]

class ConsultaRegistroVendaSchema(BaseModel):
    id_registro: int
