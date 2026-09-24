from models.material_reciclavel import MaterialReciclavel

#Service para cálculo da venda
def calcular_valor_venda(session, id_material, kg_material):
    """
        Calcula o valor em reais da venda realizada
    """
    material = session.query(MaterialReciclavel).filter(MaterialReciclavel.codigo == id_material).first()
    if not material:
            raise ValueError("Material reciclável não encontrado")
    valor = kg_material * material.valor_kg
    return valor
    