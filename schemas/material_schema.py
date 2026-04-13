from pydantic import BaseModel, Field
from typing import List, Optional
from models.material_reciclavel import MaterialReciclavel

class MaterialReciclavelSchema(BaseModel):
    codigo: int = Field(..., example=200)
    categoria: str = Field(..., example="Vidro")
    quantidade_kg: float = Field(..., example=15.5)
    valor_kg: float = Field(..., example=0.40)

def visualizar_material(material: MaterialReciclavel):
    return {
        "codigo": material.codigo,
        "categoria": material.categoria,
        "quantidade_kg": material.quantidade_kg,
        "valor_kg": material.valor_kg
    }

class ListaMateriaisSchema(BaseModel):
    materials: list[MaterialReciclavelSchema]

def listar_materiais(materiais: List[MaterialReciclavel]) -> List[MaterialReciclavel]:
     return [MaterialReciclavelSchema(
        codigo = material.codigo,
        categoria = material.categoria,
        quantidade_kg = material.quantidade_kg,
        valor_kg = material.valor_kg
    ) for material in materiais]

class ConsultaMaterialSchema(BaseModel):
    codigo: int
    
class ExclusaoMaterialSchema(BaseModel):
    id: int

class AtualizarMaterialSchema(BaseModel):
    codigo: int
    valor_kg: Optional[float] = None

class ExcluirMaterialSchema(BaseModel):
    msg: str
    codigo: int

