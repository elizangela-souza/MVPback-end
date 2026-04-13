from sqlalchemy.exc import IntegrityError

from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from models.cooperado import Cooperado
from models.material_reciclavel import MaterialReciclavel
from models.registro_triagem import RegistroTriagem
from schemas.cooperado_schema import CooperadoSchema, ConsultaCooperadoSchema, ExclusaoCooperadoSchema, ListaCooperadosSchema, AtualizarCooperadoSchema, ExcluirCooperadoSchema, visualizar_cooperado, listar_cooperados
from schemas.material_schema import ExclusaoMaterialSchema, MaterialReciclavelSchema, ConsultaMaterialSchema, ListaMateriaisSchema, AtualizarMaterialSchema, ExcluirMaterialSchema, visualizar_material, listar_materiais
from schemas.triagem_schema import RegistroTriagemSchema, ConsultaRegistroTriagemSchema, ListaTriagemSchema,visualizar_triagem, listar_triagens
from schemas.error_schema import ErrorSchema
from models import Session
from logger import logger
from service import atualizar_estoque_material

info = Info(title="API da Cooperativa de Reciclagem", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

#Tags para documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cooperado_tag = Tag(name="Cooperado", description="Operações relacionadas aos registros dos cooperados: inclusão, consulta, atualização e exclusão.")
material_tag = Tag(name="MaterialReciclavel", description="Operações relacionadas aos registros dos materias recicláveis: inclusão, consulta, atualização e exclusão.")
triagem_tag = Tag(name="RegistroTriagem", description="Operações relacionadas aos registros das triagens: inclusão e consulta")

@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

#OPERAÇÕES COOPERADO
@app.post('/cadastrar_cooperado', tags=[cooperado_tag], responses={"200": CooperadoSchema, "404": ErrorSchema})
def cadastrar_cooperado(form: CooperadoSchema):
    """
    Inclui o registro de um cooperado
    """
    cooperado = Cooperado(
        matricula = form.matricula,
        nome = form.nome,
        cpf = form.cpf,
        data_nascimento = form.data_nascimento,
        telefone = form.telefone
    )
    logger.debug(f"Incluindo registro do/a cooperado/a com a matrícula '{cooperado.matricula}' ao banco de dados.")
    try:
        session = Session()
        session.add(cooperado)
        session.commit()
        logger.debug(f"Registro de Cooperado/a '{cooperado.nome}' com a matrícula '{cooperado.matricula}' incluído ao banco de dados.")
        return visualizar_cooperado(cooperado), 200
    except IntegrityError:
        session.rollback()
        error_message = f"Já existe um cooperado com a matrícula '{cooperado.matricula}' ou CPF '{cooperado.cpf}' cadastrado."
        logger.warning(error_message)
        return {"error": error_message}, 404
    except Exception as error:
        session.rollback()
        error_mesage = f"Erro ao adicionar cooperado/a com matrícula '{cooperado.matricula}"
        logger.warning(f"{error_mesage}: {error}")
        return  {"error": error_mesage}, 404
    

@app.get('/buscar_cooperado', tags=[cooperado_tag], responses={"200": CooperadoSchema, "404": ErrorSchema})
def buscar_cooperado(query: ConsultaCooperadoSchema):
    """
    Consulta o registro de um cooperado
    """
    matricula = query.matricula
    session = Session()
    try:   
        cooperado = session.query(Cooperado).filter(Cooperado.matricula==matricula).first()
        if cooperado:
            logger.debug(f"Registro de cooperado/a com matrícula '{matricula}' encontrado")
            return visualizar_cooperado(cooperado), 200
        else:
            error_mesage = f"Registro de cooperado com a matrícula {matricula} não encontrado"
            logger.warning(f"Erro ao consultar registro com a matrícula {matricula}")
            return  {"error": error_mesage}, 404
    except Exception as e:
        logger.error(f"Erro interno ao consultar cooperado {matricula}: {e}")
        return {"error": "Falha interna ao consultar cooperado"}, 500
    finally:
        session.close()


@app.get('/buscar_cooperados', tags=[cooperado_tag], responses={"200": ListaCooperadosSchema, "500": ErrorSchema})
def buscar_cooperados():
    """
    Consulta todos os registro da tabela cooperado
    """
    session = Session()
    try:
        cooperados = session.query(Cooperado).all()
        if cooperados:
            logger.debug(f"Total de cooperados encontrados: {len(cooperados)}")
            return {"cooperados": [visualizar_cooperado(cooperado) for cooperado in cooperados]}, 200
        else:
            error_mesage = "Nenhum registro de cooperado encontrado"
            logger.warning("Nenhum registro de cooperado encontrado")
            return  {"cooperados": []}, 200
    except Exception as error:
        logger.error(f"Erro ao consultar registros dos cooperados: {error_mesage}")
        return {"error": "Falha ao consultar o banco"}, 500
    finally:
        session.close()


@app.put('/atualizar_cooperado', tags=[cooperado_tag], responses={"200": CooperadoSchema, "404": ErrorSchema})
def atualizar_cooperado(form: AtualizarCooperadoSchema):
    """
    Atualiza o registro de um cooperado
    """
    matricula = form.matricula
    session = Session()
    cooperado = session.query(Cooperado).filter(Cooperado.matricula == matricula).first()
    if cooperado:
        if form.nome is not None:
            cooperado.nome = form.nome
        if form.telefone is not None:
            cooperado.telefone = form.telefone
        session.commit()
        logger.debug(f"Dados do/a cooperado/a com a matrícula '{matricula}' atualizados")
        return visualizar_cooperado(cooperado), 200
    else:
        error_mesage = f"Cooperado com a matrícula {matricula} não encontrado"
        logger.warning(f"Erro ao atualizar dados do/a cooperado/a com a matrícula '{matricula}', {error_mesage}")
        return  {"error": error_mesage}, 404


@app.delete('/deletar_cooperado', tags=[cooperado_tag], responses={"200": ExcluirCooperadoSchema, "404": ErrorSchema})
def deletar_cooperado(query: ExclusaoCooperadoSchema):
    """
    Exclui o registro de um cooperado
    """
    matricula = query.id
    session = Session()
    try:
        count = session.query(Cooperado).filter(Cooperado.matricula == matricula).delete()
        session.commit()
        if count: 
            logger.debug(f"Exclusão do registro do/a cooperado/a com a matrícula {matricula} realizada com sucesso")
            return {"mesage": f"Cooperado com a matrícula {matricula} excluído com sucesso do banco de dados!"}, 200
        else:
            logger.debug(f"Erro na exclusão: matrícula {matricula} não encontrada")
            return {"error": "Registro não encontrado"}, 404
    except Exception as e:
        logger.error(f"Erro interno ao excluir cooperado {matricula}: {e}")
        return {"error": "Falha interna ao excluir cooperado"}, 500
    finally:
        session.close()


#OPERAÇÕES MATERIAL RECICLÁVEL
@app.post('/cadastrar_material', tags=[material_tag], responses={"200": MaterialReciclavelSchema, "404": ErrorSchema})
def cadastrar_material(form: MaterialReciclavelSchema):
    """
    Inclui o registro de um material reciclável
    """  
    material = MaterialReciclavel(
        codigo = form.codigo,
        categoria = form.categoria,
        quantidade_kg = form.quantidade_kg,
        valor_kg = form.valor_kg
    )
    logger.debug(f"Incluindo material '{material.categoria}' com código '{material.codigo}' ao banco de dados.")
    try:
        session = Session()
        session.add(material)
        session.commit()
        logger.debug(f"Material '{material.categoria}' com código '{material.codigo}' incluído ao banco de dados.")
        return visualizar_material(material), 200
    except IntegrityError:
        session.rollback()
        error_message = f"Já existe um material com código '{material.codigo}' cadastrado."
        logger.warning(error_message)
        return {"error": error_message}, 404
    except Exception as error:
        error_mesage = f"Erro ao incluir material reciclável com código '{material.codigo}"
        logger.warning(f"{error_mesage}: {error}")
        return {"error": error_mesage}, 404
    finally:
        session.close()

@app.get('/buscar_material', tags=[material_tag], responses={"200": MaterialReciclavelSchema, "404": ErrorSchema})
def buscar_material(query: ConsultaMaterialSchema):
    """
    Consulta o registro de um material
    """
    codigo = query.codigo
    session = Session()
    try:   
        material = session.query(MaterialReciclavel).filter(MaterialReciclavel.codigo==codigo).first()
        if material:
            logger.debug(f"Registro de material/a com código '{codigo}' encontrado")
            return visualizar_material(material), 200
        else:
            error_mesage = f"Registro de material com a código {codigo} não encontrado"
            logger.warning(f"Erro ao consultar registro com a código {codigo}")
            return  {"error": error_mesage}, 404
    except Exception as e:
        logger.error(f"Erro interno ao consultar material {codigo}: {e}")
        return {"error": "Falha interna ao consultar material"}, 500
    finally:
        session.close()

@app.get('/buscar_materiais', tags=[material_tag], responses={"200": ListaMateriaisSchema, "500": ErrorSchema})
def buscar_materiais():
    """
    Consulta todos os registros da tabela material reciclável
    """
    session = Session()
    try:
        materiais = session.query(MaterialReciclavel).all()
        if materiais:
            logger.debug(f"Total de materiais recicláveis encontrados: {len(materiais)}")
            return {"materiais": [visualizar_material(material) for material in materiais]}, 200
        else:
            error_mesage = "Nenhum registro de material reciclável encontrado"
            logger.warning(f"Erro ao consultar materiais: {error_mesage}")
            return {"materiais": []}, 200
    except Exception as error:
        logger.error(f"Erro ao consultar registros dos materiais: {error}")
        return {"error": "Falha ao consultar o banco"}, 500
    finally:
        session.close()


@app.put('/atualizar_material', tags=[material_tag], responses={"200": MaterialReciclavelSchema, "404": ErrorSchema})
def atualizar_material(form: AtualizarMaterialSchema):
    """
    Atualiza o registro de um material
    """
    codigo = form.codigo
    session = Session()
    material = session.query(MaterialReciclavel).filter(MaterialReciclavel.codigo == codigo).first()
    if material:
        if form.valor_kg is not None:
            material.valor_kg = form.valor_kg
        session.commit()
        logger.debug(f"Dados do material com a código '{codigo}' atualizados")
        return visualizar_material(material), 200
    else:
        error_mesage = f"material com a código {codigo} não encontrado"
        logger.warning(f"Erro ao atualizar dados do/a material/a com a código '{codigo}', {error_mesage}")
        return  {"error": error_mesage}, 404


@app.delete('/excluir_material', tags=[material_tag], responses={"200": ExcluirMaterialSchema, "404": ErrorSchema})
def excluir_material(query: ExclusaoMaterialSchema):
    """
    Exclui o registro de um material reciclável
    """
    codigo = query.id
    session = Session()
    try:
        count = session.query(MaterialReciclavel).filter(MaterialReciclavel.codigo == codigo).delete()
        session.commit()
        if count:
            logger.debug(f"Exclusão do material com código {codigo} realizada com sucesso")
            return {"mesage": f"Material reciclável com o código {codigo} excluído com sucesso"}, 200
        else:
            logger.debug(f"Erro na exclusão do material reciclável de código {codigo}")
            return {"error": "Registro não encontrado"}, 404
    except Exception as e:
        logger.error(f"Erro interno ao excluir material com id {codigo}: {e}")
        return {"error": "Falha interna ao excluir cooperado"}, 500
    finally:
        session.close()

#OPERAÇÕES REGISTRO TRIAGEM
@app.post('/cadastrar_triagem', tags=[triagem_tag], responses={"200": RegistroTriagemSchema, "404": ErrorSchema})
def cadastrar_triagem(form: RegistroTriagemSchema):
    """
    Inclui o registro de triagem
    """
    session = Session()
    try:
        # Verifica se o cooperado existe
        cooperado = session.query(Cooperado).filter(Cooperado.matricula==form.id_cooperado).first()
        if not cooperado:
            return {"error": "Cooperado não encontrado"}, 404

        # Verifica se o material existe
        material = session.query(MaterialReciclavel).filter(MaterialReciclavel.codigo==form.id_material).first()
        if not material:
            return {"error": "Material não encontrado"}, 404

        triagem = RegistroTriagem(
            id_cooperado = form.id_cooperado,
            id_material = form.id_material,
            data_triagem = form.data_triagem,
            kg_material = form.kg_material
        )
        session.add(triagem)
       
        """
        Atualiza o estoque (quantidade em Kg) dos materiais recicláveis após o registro da triagem
        """
        atualizar_estoque_material(
            session=session, 
            id_material=triagem.id_material, 
            kg_material=triagem.kg_material, 
            tipoRegistro="triagem"
        )
        
        session.commit()

        logger.debug(f"Registro de triagem '{triagem.id_registro}' incluído e estoque atualizado para material '{triagem.id_material}'.")
        return {"triagem": visualizar_triagem(triagem)}, 200
    except IntegrityError:
        session.rollback()
        return {"error": "Cooperado ou Material não existem"}, 404
    except ValueError as error:
        session.rollback()
        logger.warning(f"Erro ao incluir triagem")
        return {"error": str(error)}, 404
    except Exception as error:
        session.rollback() 
        logger.warning(f"Erro ao incluir registro da triagem para cooperado'{form.id_cooperado}' e material {form.id_material}")
        return {"error": "Erro interno: " + str(error)}, 500
    finally:
        session.close()


@app.get('/buscar_triagens', tags=[triagem_tag], responses={"200": ListaTriagemSchema, "500": ErrorSchema})
def buscar_triagens():
    """
    Consulta todos os registros da tabela de triagem
    """
    session = Session()
    try:
        triagens = session.query(RegistroTriagem).all()
        if triagens:
            logger.debug(f"Total de registros de triagens encontrados: {len(triagens)}")
            return {"triagens": [visualizar_triagem(triagem) for triagem in triagens]}, 200
        else:
            error_message = "Nenhum registro de triagem encontrado"
            logger.warning(f"Erro ao consultar registro de triagens: {error_message}")
            return {"triagens": []}, 200
    except Exception as error:
        logger.error(f"Erro ao consultar registros dos cooperados: {error}")
        return {"error": "Falha ao consultar o banco"}, 500
    finally:
        session.close()
