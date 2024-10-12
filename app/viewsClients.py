from fasthtml.common import Titled, P, Button, Ul, Li, Div 
from db.models import Cliente, Consultor, Pedido, Avaliacao, Agenda, Session  
from auth.decorators.goodcookies import goodcookies
from sqlalchemy import or_, func
from starlette.responses import JSONResponse  

# Função para fazer pedido de consultoria
async def fazer_pedido_consulta(req, consultor_id: int):

    # Debug: Verificar se o consultor_id foi recebido corretamente
    print("consultor_id recebido do cookie:", consultor_id)

    # Se o consultor_id não estiver presente, retornar um erro
    if not consultor_id:
        return Titled("Erro", P("Consultor ID não encontrado nos cookies."))

    # Extraindo o cliente_email do JWT
    cliente_email = req.state.user["sub"]  # Cliente logado extraído do JWT

    session = Session()
    cliente = session.query(Cliente).filter(Cliente.email == cliente_email).first()

    if not cliente:
        session.close()
        return Titled("Erro", P("Cliente não encontrado."))

    try:
        # Criar o pedido de consultoria com o consultor_id e cliente_id
        pedido = Pedido(consultor_id=consultor_id, cliente_id=cliente.id, status="pendente")
        session.add(pedido)
        session.commit()

        session.close()
        return Titled("Sucesso", P("Pedido de consultoria enviado com sucesso!"))
    except Exception as e:
        session.rollback()
        session.close()
        return Titled("Erro", P(f"Ocorreu um erro ao criar o pedido: {str(e)}"))

# Função para buscar consultores com filtros
async def buscar_consultores(req):
        form_data = await req.form()
        termo_pesquisa = form_data.get("termo")  # Termo para busca por nome ou área de atuação
        avaliacao_minima = form_data.get("avaliacao_minima")  # Filtro de avaliação mínima
        apenas_disponiveis = form_data.get("apenas_disponiveis")  # Filtro de disponibilidade

        session = Session()

        # Query base para buscar consultores
        query = session.query(Consultor).filter(
            or_(
                Consultor.nome.ilike(f'%{termo_pesquisa}%'),
                Consultor.atuacao.ilike(f'%{termo_pesquisa}%')
            )
        )

        # Filtro por avaliação mínima
        if avaliacao_minima:
            query = query.join(Avaliacao).group_by(Consultor.id).having(func.avg(Avaliacao.nota) >= avaliacao_minima)

        # Filtro de disponibilidade (consultores com agenda disponível)
        if apenas_disponiveis:
            query = query.outerjoin(Agenda).filter(Agenda.id == None)  # Consultores sem agenda vinculada

        consultores = query.all()
        session.close()

        if not consultores:
            return Titled("Nenhum consultor encontrado.")

        # Gerar a lista de consultores em HTML
        consultores_html = Ul(*[
            Li(f"{consultor.nome} - {consultor.atuacao}",
                hx_get=f"/detalhes_consultor/{consultor.id}",
                hx_target="#detalhes-consultor",
                hx_swap="outerHTML"
            ) for consultor in consultores
        ])

        return Titled("Lista de Consultores", consultores_html)

 
# Função para exibir os detalhes do consultor
async def detalhes_consultor(req, consultor_id: int):
    session = Session()

    # Definir cookie com consultor_id para futuras interações
    response = JSONResponse(content={"message": "Armazenamento realizado com sucesso!", "consultor ID": consultor_id})
    response.set_cookie(key="consultor_id", value=str(consultor_id), httponly=True)  # Corrigido para garantir o valor correto

    # Buscar consultor pelo ID
    consultor = session.query(Consultor).filter(Consultor.id == consultor_id).first()
    session.close()

    if not consultor:
        return Titled("Erro", P("Consultor não encontrado."), status_code=404)

    # Retornar os detalhes do consultor em HTML
    detalhes_html = Div(
        P(f"Nome: {consultor.nome}"),
        P(f"Área de Atuação: {consultor.atuacao}"),
        Button("Solicitar Consultoria", hx_post=f"/fazer_pedido_consulta/{consultor.id}", hx_trigger="click" )
    )

    return Titled("Detalhes do Consultor", detalhes_html)
