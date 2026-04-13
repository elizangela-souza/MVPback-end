from models.material_reciclavel import MaterialReciclavel

#Service para regra de negócio
def atualizar_estoque_material(session, id_material, kg_material, tipoRegistro):
    """
    Atualização de quantidade de material reciclável(estoque da cooperativa)
    """
    material = session.query(MaterialReciclavel).filter(MaterialReciclavel.codigo == id_material).first()
    if not material:
        raise ValueError("Material reciclável não encontrado")
    if  tipoRegistro == "venda":
        material.atualizar_quantidade(-kg_material)
    elif tipoRegistro == "triagem":
        material.atualizar_quantidade(+kg_material)
    else: 
        raise ValueError(f"Tipo de registro inválido: {tipoRegistro}")
    return material

