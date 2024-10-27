from fasthtml.common import Titled, P, Button, Ul, Li, Div, H3, Form, Label, Input
from db.models import Cliente, Consultor, Pedido, Avaliacao, Agenda, Session
from sqlalchemy import or_, func 
from starlette.responses import JSONResponse

# Dados do cliente
async def get_client_info(req):
    cliente_email = req.state.user["sub"]
    session = Session()
    client = session.query(Cliente).filter_by(email=cliente_email).first()
    return client


# Função para exibir os detalhes do consultor
async def detalhes_consultor(req, consultor_id: int):
    session = Session()

    # Definir cookie com consultor_id para futuras interações
    response = JSONResponse(content={"message": "Armazenamento realizado com sucesso!", "consultor ID": consultor_id})
    response.set_cookie(key="consultor_id", value=str(consultor_id), httponly=True)

    # Buscar consultor pelo ID
    consultor = session.query(Consultor).filter(Consultor.id == consultor_id).first()
    session.close()

    if not consultor:
        return Titled("Erro", P("Consultor não encontrado.", cls="text-center text-red-500 text-lg"), status_code=404)

    # Retornar os detalhes do consultor em HTML com TailwindCSS
    detalhes_html = Div(
        P(f"Nome: {consultor.nome}", cls="text-lg font-semibold text-gray-800"),
        P(f"Área de Atuação: {consultor.atuacao}", cls="text-md text-gray-600 mb-4"),
        Button(
            "Solicitar Consultoria",
            hx_post=f"/fazer_pedido_consulta/{consultor.id}",
            hx_trigger="click",
            cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        ),
        cls="p-6 bg-white rounded-lg shadow-md"
    )

    return Titled("Detalhes do Consultor", detalhes_html, cls="text-center text-2xl font-bold text-purple-700 mb-6")


async def buscar_consultores_cliente(req):
    form_data = await req.form()  # Obter dados do formulário
    termo_pesquisa = form_data.get("termo")
    avaliacao_minima = form_data.get("avaliacao_minima")
    apenas_disponiveis = form_data.get("apenas_disponiveis") == "true"

    session = Session()

    # Construir a consulta com filtros
    query = session.query(Consultor).filter(
        or_(
            Consultor.nome.ilike(f'%{termo_pesquisa}%'),
            Consultor.atuacao.ilike(f'%{termo_pesquisa}%')
        )
    )

    if avaliacao_minima:
        query = query.join(Avaliacao).group_by(Consultor.id).having(func.avg(Avaliacao.nota) >= avaliacao_minima)

    if apenas_disponiveis:
        query = query.outerjoin(Agenda).filter(Agenda.id == None)

    consultores = query.all()
    session.close()

    if not consultores:
        return Titled("Nenhum consultor encontrado.", cls="text-center text-gray-500 text-xl font-semibold py-4")

    # Gerar a lista de consultores em HTML com TailwindCSS
    consultores_html = Ul(*[
        Li(
            f"{consultor.nome} - {consultor.atuacao}",
            hx_get=f"/detalhes_consultor/{consultor.id}",
            hx_target="#detalhes-consultor",
            hx_swap="outerHTML",
            cls="p-4 border-b border-gray-300 hover:bg-gray-100 cursor-pointer text-gray-800 font-medium"
        ) for consultor in consultores
    ], id='detalhes-consultor', cls="bg-white shadow-md rounded-lg")

    return Div(
        consultores_html,
        id='cards-section',
        cls="max-w-2xl mx-auto my-8 p-6 bg-gray-50 rounded-lg shadow-lg"
    )
async def listar_historico_consultas_cliente(req):
    session = Session()
    cliente_email = req.state.user["sub"]
    cliente = session.query(Cliente).filter(Cliente.email == cliente_email).first()

    consultas = session.query(Pedido).filter(Pedido.cliente_id == cliente.id).order_by(Pedido.created_at.desc()).all()
    consulta_list = [
        {"id": consulta.id, "consultor": consulta.consultor.nome, "status": consulta.status, "data": consulta.created_at.strftime("%d/%m/%Y")}
        for consulta in consultas
    ]
    session.close()
    return consulta_list
 
async def fazer_pedido_consulta(req, consultor_id: int):
    cliente_email = req.state.user["sub"]
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.email == cliente_email).first()

    try:
        pedido = Pedido(consultor_id=consultor_id, cliente_id=cliente.id, status="pendente")
        session.add(pedido)
        session.commit()
        session.close()
        return Titled("Sucesso", P("Pedido de consultoria enviado com sucesso!"))
    except Exception as e:
        session.rollback()
        session.close()
        return Titled("Erro", P(f"Ocorreu um erro ao criar o pedido: {str(e)}"))
