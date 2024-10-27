from fasthtml.common import Titled, Tr, Td, P, Button, Form, Table, Th, Thead, Tbody, Fieldset, Input, Label, Div
from sqlalchemy.exc import IntegrityError  
from starlette.responses import JSONResponse, RedirectResponse
from sqlalchemy.exc import IntegrityError
from db.models import Agenda, Cliente, Consultor, Pedido, Session
from auth.utils import gerar_token_jwt, hash_senha, verificar_senha 
from services.notice import enviar_email_notificacao
from datetime import datetime
from sqlalchemy import func   
  

async def obter_agendas_recentes(req):
    session = Session()
    consultor_email = req.state.user["sub"]  # Extrai o e-mail do consultor autenticado

    # Identifica o consultor logado
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
    if not consultor:
        session.close()
        return []
    print(consultor.nome)

    # Busca as agendas associadas ao consultor, ordenadas pela data de criação, limitando a um número específico, como 5
    agendas = (
        session.query(Agenda)
        .join(Pedido, Agenda.pedido_id == Pedido.id)
        .filter(Pedido.consultor_id == consultor.id)
        .order_by(Agenda.data.desc())
        .limit(5)  # Limita para exibir apenas as 5 agendas mais recentes
        .all()
    )

    # Formata os dados da agenda para serem usados no dashboard
    agenda_list = [
        {
            "id": agenda.id,
            "data": agenda.data.strftime("%d/%m/%Y"),
            "horario": agenda.horario.strftime("%H:%M"),
            "cliente": agenda.pedido.cliente.nome if agenda.pedido else "N/A"
        }
        for agenda in agendas
    ]

    session.close()
    return agenda_list

async def contar_agendas_ocupadas(req):
    session = Session()
    consultor_email = req.state.user["sub"]  
    
    # Conta as agendas ocupadas associadas ao consultor autenticado
    count = session.query(Agenda).filter(
        Agenda.pedido_id.isnot(None),
        Agenda.consultor_email == consultor_email
    ).count()
    
    session.close()
    return count

async def contar_agendas_livres(req):
    session = Session()
    consultor_email = req.state.user["sub"]

    # Conta as agendas que não têm um pedido associado (ou seja, estão livres)
    count = session.query(Agenda).filter(Agenda.pedido_id.is_(None)).count()
    session.close()
    return count

async def contar_clientes_atendidos(req):
    session = Session()
    consultor_email = req.state.user["sub"]

    # Conta os clientes atendidos por este consultor
    count = session.query(Pedido).filter(Pedido.status == "atendido", Pedido.consultor.has(email=consultor_email)).count()
    session.close()
    return count

async def contar_pedidos_pendentes(req):
    session = Session()
    consultor_email = req.state.user["sub"]

    # Conta os pedidos de consulta que estão pendentes para este consultor
    count = session.query(Pedido).filter(Pedido.consultor.has(email=consultor_email), Pedido.status == "pendente").count()
    session.close()
    return count

# Dados do cliente
async def consultor_info(req):
    consultor_email = req.state.user["sub"]
    session = Session()
    consultor = session.query(Consultor).filter_by(email=consultor_email).first()
    return consultor


async def cadastrar_consultor(req):
    form_data = await req.form()
    
    nome = form_data.get("nome")
    email = form_data.get("email")
    atuacao = form_data.get("atuacao")
    senha = form_data.get("senha")

    if not nome or not email or not atuacao or not senha:
        return JSONResponse(content={"message": "Todos os campos são obrigatórios."}, status_code=400)

    senha_hashed = hash_senha(senha)

    session = Session()
    consultor = Consultor(nome=nome, email=email, atuacao=atuacao, senha=senha_hashed)
    
     
    try:
        session.add(consultor)
        session.commit()
        return RedirectResponse(url='/consultant', status_code=307)
    except IntegrityError:
        session.rollback()
        return RedirectResponse(url='/exist', status_code=307)
    finally:
        session.close()


async def cadastrar_cliente(req):
    form_data = await req.form()
    
    nome = form_data.get("nome")
    email = form_data.get("email")
    senha = form_data.get("senha")

    if not nome or not email or not senha:
        return JSONResponse(content={"message": "Todos os campos são obrigatórios."}, status_code=400)

    senha_hashed = hash_senha(senha)

    session = Session()
    cliente = Cliente(nome=nome, email=email, senha=senha_hashed)
    
    try:
        session.add(cliente)
        session.commit()
        return RedirectResponse(url='/client', status_code=307)
         
    except IntegrityError:
        session.rollback()
        return RedirectResponse(url='/exist', status_code=307)
        session.close()


async def login(req):
    form_data = await req.form()
    email = form_data.get("email")
    senha = form_data.get("senha")

    if not email or not senha:
        return JSONResponse(content={"message": "Todos os campos são obrigatórios."}, status_code=400)

    session = Session()

    # Verifica se o usuário é consultor
    consultor = session.query(Consultor).filter(Consultor.email == email).first()
    if consultor and verificar_senha(senha, consultor.senha):
        token = gerar_token_jwt(email, "consultor")
          
        res = RedirectResponse(url='/connected_as_a_consultant', status_code=303)
        res.set_cookie(key="access_token", value=token, httponly=True) 
        session.close()
        return res

    # Verifica se o usuário é cliente
    cliente = session.query(Cliente).filter(Cliente.email == email).first()
    if cliente and verificar_senha(senha, cliente.senha):
        token = gerar_token_jwt(email, "cliente")
        response = RedirectResponse(url='/dashboard_cliente', status_code=307)
         
        response.set_cookie(key="access_token", value=token, httponly=True)
        session.close()
        return response
                    
    session.close()
    return JSONResponse(content={"message": "Credenciais inválidas."}, status_code=401)


async def criar_agenda(req):
    form_data = await req.form()
    assunto = form_data.get("assunto")
    data = form_data.get("data")
    horario = form_data.get("horario")

    if not assunto or not data or not horario:
        return JSONResponse(content={"message": "Todos os campos são obrigatórios."}, status_code=400)

    session = Session()
    consultor_email = req.state.user["sub"]  # Extrair email do consultor do token JWT

    # Buscar o consultor
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
    
    if not consultor:
        session.close()
        return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

    agenda = Agenda(
        pedido_id=None,  # Pode ser associado futuramente
        assunto=assunto,
        data=data,
        horario=horario
    )
    session.add(agenda)
    
    try:
        session.commit()

        # Enviar notificação para o consultor
        mensagem = f"Olá {consultor.nome},\n\nUma nova agenda foi criada:\nAssunto: {assunto}\nData: {data}\nHorário: {horario}\n"
        enviar_email_notificacao(consultor.email, "Nova Agenda Criada", mensagem)

        return JSONResponse(content={"message": "Agenda criada com sucesso!"}, status_code=201)
    except Exception as e:
        session.rollback()
        return JSONResponse(content={"message": "Erro ao criar agenda.", "error": str(e)}, status_code=500)
    finally:
        session.close()

async def minhas_agendas(req):
    session = Session()
    consultor_email = req.state.user["sub"]  # Email do consultor extraído do token

    # Buscar o consultor logado
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
    if not consultor:
        session.close()
        return Titled(
            "Erro",
            P("Consultor não encontrado.", cls="text-center text-red-500 text-lg")
        )

    # Buscar agendas do consultor
    agendas = session.query(Agenda).filter(Agenda.pedido.has(consultor_id=consultor.id)).all()

    if not agendas:
        session.close()
        return Titled(
            "Minhas Agendas",
            P("Nenhuma agenda encontrada.", cls="text-center text-gray-500 text-lg")
        )

    # Gerar tabela de agendas, incluindo o campo "assunto"
    agenda_rows = [
        Tr(
            Td(a.assunto, cls="p-4 text-gray-700"),
            Td(str(a.data), cls="p-4 text-gray-600"),
            Td(str(a.horario), cls="p-4 text-gray-600"),
            Td(
                Button(
                    "Editar",
                    hx_get=f"/form_editar_agenda/{a.id}",  # Utiliza HTMX para carregar o formulário de edição
                    hx_target="#main-panel",  # ID do elemento de destino onde o formulário de edição será carregado
                    hx_swap="outerHTML",
                    cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-3 rounded"
                ),
                cls="text-center"
            ),
            Td(
                Form(
                    method="post",
                    action=f"/eliminar_agenda/{a.id}",
                    hx_post=f"/eliminar_agenda/{a.id}",  # Configuração HTMX para excluir o item
                    hx_target="#main-panel",  # ID do elemento onde a lista de agendas será atualizada
                    hx_swap="outerHTML"
                )(
                    Button(
                        "Eliminar",
                        type="submit",
                        cls="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded"
                    )
                ),
                cls="text-center"
            )
        ) for a in agendas
    ]


    session.close()

    return Div(
        Button(
            '▼ Agendas',
            cls='text-2xl ml-10 font-bold text-purple-700 mb-4',
            id='toggle-button',
            onclick="toggleCardsSection('Agendas')"
        ),
        Table(
            Thead(
                Tr(
                    Th("Assunto", cls="p-4 border-b-2 border-gray-200 text-left text-gray-800"),
                    Th("Data", cls="p-4 border-b-2 border-gray-200 text-left text-gray-800"),
                    Th("Horário", cls="p-4 border-b-2 border-gray-200 text-left text-gray-800"),
                    Th("Editar", cls="p-4 border-b-2 border-gray-200 text-center text-gray-800"),
                    Th("Eliminar", cls="p-4 border-b-2 border-gray-200 text-center text-gray-800")
                )
            ),
            Tbody(*agenda_rows),
            cls="min-w-full bg-white rounded-lg shadow-md"
        ),
        cls="p-6 bg-gray-50 rounded-lg shadow-lg", id='main-panel'
    )

async def buscar_agendas_por_assunto(req):
    form_data = await req.form()
    assunto = form_data.get("assunto")
    
    if not assunto:
        return JSONResponse(content={"message": "Assunto é obrigatório."}, status_code=400)

    session = Session()
    consultor_email = req.state.user["sub"]  # Pega o email do consultor através do token JWT
    
    # Buscar consultor logado
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
    if not consultor:
        session.close()
        return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

    # Filtrar agendas do consultor pelo assunto
    agendas = session.query(Agenda).filter(Agenda.pedido.has(consultor_id=consultor.id), Agenda.assunto.ilike(f'%{assunto}%')).all()

    if not agendas:
        session.close()
        return JSONResponse(content={"message": "Nenhuma agenda encontrada para o assunto informado."}, status_code=404)

    # Retornar os detalhes das agendas encontradas
    agenda_list = [
        {
            "id": agenda.id,
            "assunto": agenda.assunto,
            "data": str(agenda.data),
            "horario": str(agenda.horario)
        } for agenda in agendas
    ]
    
    session.close()
    return JSONResponse(content={"agendas": agenda_list}, status_code=200)
 

async def duplicar_agenda(req, agenda_id: int):
    session = Session()
    consultor_email = req.state.user["sub"]  # Obtém o email do consultor a partir do token JWT

    try:
        # Buscar o consultor logado
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        if not consultor:
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        # Buscar a agenda que o consultor deseja duplicar
        agenda_original = session.query(Agenda).filter(Agenda.id == agenda_id, Agenda.pedido.has(consultor_id=consultor.id)).first()
        if not agenda_original:
            return JSONResponse(content={"message": "Agenda não encontrada ou não pertence ao consultor."}, status_code=404)

        # Criar uma nova instância da Agenda duplicando os detalhes da original
        nova_agenda = Agenda(
            pedido_id=agenda_original.pedido_id,  # Mantém o pedido original ou pode ser None
            assunto=agenda_original.assunto,
            data=agenda_original.data,
            horario=agenda_original.horario
        )

        session.add(nova_agenda)
        session.commit()

        return JSONResponse(content={"message": "Agenda duplicada com sucesso!", "nova_agenda_id": nova_agenda.id}, status_code=201)

    except Exception as e:
        session.rollback()
        return JSONResponse(content={"message": "Erro ao duplicar a agenda.", "error": str(e)}, status_code=500)

    finally:
        session.close()

 
async def listar_agendas_concluidas(req):
    session = Session()
    consultor_email = req.state.user["sub"]  # Extrai o email do consultor do token JWT

    try:
        # Buscar o consultor logado
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        if not consultor:
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        # Buscar todas as agendas do consultor que já passaram da data atual
        agora = datetime.now().date()
        agendas_concluidas = session.query(Agenda).filter(
            Agenda.pedido.has(consultor_id=consultor.id),
            Agenda.data < agora
        ).all()

        if not agendas_concluidas:
            return JSONResponse(content={"message": "Nenhuma agenda concluída encontrada."}, status_code=404)

        # Listar as agendas concluídas
        agenda_list = [
            {
                "id": agenda.id,
                "assunto": agenda.assunto,
                "data": str(agenda.data),
                "horario": str(agenda.horario)
            } for agenda in agendas_concluidas
        ]

        return JSONResponse(content={"agendas_concluidas": agenda_list}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": "Erro ao buscar agendas concluídas.", "error": str(e)}, status_code=500)

    finally:
        session.close()


async def eliminar_agenda(req, agenda_id: int):
    session = Session()
    consultor_email = req.state.user["sub"]  # Email do consultor extraído do token JWT

    try:
        # Buscar o consultor pelo email contido no payload do token JWT
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        
        if not consultor:
            session.close()
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        # Buscar a agenda pelo ID e verificar se pertence ao consultor via Pedido
        agenda = session.query(Agenda).filter(Agenda.id == agenda_id).first()

        if not agenda or agenda.pedido.consultor_id != consultor.id:
            return JSONResponse(content={"message": "Agenda não encontrada ou não pertence ao consultor."}, status_code=404)
        
        # Eliminar a agenda
        session.delete(agenda)
        session.commit()

        return JSONResponse(content={"message": "Agenda eliminada com sucesso!"}, status_code=200)
    
    except Exception as e:
        session.rollback()
        return JSONResponse(content={"message": "Erro ao eliminar a agenda.", "error": str(e)}, status_code=500)
    
    finally:
        session.close()

async def form_editar_agenda(req, agenda_id: int):
    session = Session()
    consultor_email = req.state.user["sub"]

    # Buscar o consultor logado pelo email contido no token
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()

    if not consultor:
        session.close()
        return Titled("Erro", P("Consultor não encontrado."))

    # Buscar a agenda pelo ID e verificar se pertence ao consultor logado
    agenda = session.query(Agenda).filter(Agenda.id == agenda_id, Agenda.pedido.has(consultor_id=consultor.id)).first()

    if not agenda:
        session.close()
        return Titled("Erro", P("Agenda não encontrada."))

    # Retornar o formulário com os dados atuais da agenda, incluindo o campo "assunto"
    session.close()

    return Titled("Editar Agenda",
        Form(method="post", action=f"/atualizar_agenda/{agenda.id}")(
            Fieldset(
                Label("Assunto: ", Input(name="assunto", type="text", value=str(agenda.assunto), required=True)),
                Label("Data: ", Input(name="data", type="date", value=str(agenda.data), required=True)),
                Label("Horário: ", Input(name="horario", type="time", value=str(agenda.horario), required=True))
            ),
            Button("Atualizar Agenda", type="submit")
        )
    )

async def atualizar_agenda(req, agenda_id: int):
    form_data = await req.form()
    novo_assunto = form_data.get("assunto")
    nova_data = form_data.get("data")
    novo_horario = form_data.get("horario")

    if not novo_assunto or not nova_data or not novo_horario:
        return JSONResponse(content={"message": "Assunto, data e horário são obrigatórios."}, status_code=400)

    session = Session()
    consultor_email = req.state.user["sub"]

    try:
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        
        if not consultor:
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        agenda = session.query(Agenda).filter(Agenda.id == agenda_id, Agenda.pedido.has(consultor_id=consultor.id)).first()
        
        if not agenda:
            return JSONResponse(content={"message": "Agenda não encontrada ou não pertence ao consultor."}, status_code=404)

        agenda.assunto = novo_assunto
        agenda.data = nova_data
        agenda.horario = novo_horario 

        session.commit()

        # Enviar notificação de atualização
        mensagem = f"Olá {consultor.nome},\n\nSua agenda foi atualizada:\nNovo Assunto: {novo_assunto}\nNova Data: {nova_data}\nNovo Horário: {novo_horario}\n"
        enviar_email_notificacao(consultor.email, "Agenda Atualizada", mensagem)

        return JSONResponse(content={"message": "Agenda atualizada com sucesso!"}, status_code=200)
    
    except Exception as e:
        session.rollback()
        return JSONResponse(content={"message": "Erro ao atualizar a agenda.", "error": str(e)}, status_code=500)
    
    finally:
        session.close()

async def template_editar_agenda(req, agenda_id: int):
    session = Session()
    consultor_email = req.state.user["sub"]

    # Buscar o consultor logado pelo email contido no token
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()

    if not consultor:
        session.close()
        return Titled("Erro", P("Consultor não encontrado."))

    # Buscar a agenda pelo ID e verificar se pertence ao consultor logado
    agenda = session.query(Agenda).filter(Agenda.id == agenda_id, Agenda.pedido.has(consultor_id=consultor.id)).first()

    if not agenda:
        session.close()
        return Titled("Erro", P("Agenda não encontrada."))

    # Fechar a sessão
    session.close()

    # Retornar o formulário com os dados atuais da agenda, incluindo o campo "assunto"
    return Titled("Editar Agenda",
        Form(
            method="post",
            action=f"/atualizar_agenda/{agenda.id}",
            cls="space-y-6 bg-white p-6 rounded-lg shadow-lg"
        )(
            Fieldset(
                Label(
                    "Assunto:",
                    Input(
                        name="assunto",
                        type="text",
                        value=str(agenda.assunto),
                        required=True,
                        cls="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                    ),
                    cls="block text-gray-700 font-bold mb-2"
                ),
                Label(
                    "Data:",
                    Input(
                        name="data",
                        type="date",
                        value=str(agenda.data),
                        required=True,
                        cls="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                    ),
                    cls="block text-gray-700 font-bold mb-2"
                ),
                Label(
                    "Horário:",
                    Input(
                        name="horario",
                        type="time",
                        value=str(agenda.horario),
                        required=True,
                        cls="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500"
                    ),
                    cls="block text-gray-700 font-bold mb-2"
                ),
                cls="space-y-4"
            ),
            Button(
                "Atualizar Agenda",
                type="submit",
                cls="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded-lg"
            )
        )
    )

async def gerar_relatorio_agendas(req):
    session = Session()
    consultor_email = req.state.user["sub"]  # Obtém o email do consultor do token JWT

    try:
        # Buscar o consultor logado
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        if not consultor:
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        # Contar o número de agendas por assunto
        relatorio_por_assunto = session.query(
            Agenda.assunto,
            func.count(Agenda.id).label("total")
        ).filter(Agenda.pedido.has(consultor_id=consultor.id)).group_by(Agenda.assunto).all()

        # Contar o número de agendas por data
        relatorio_por_data = session.query(
            Agenda.data,
            func.count(Agenda.id).label("total")
        ).filter(Agenda.pedido.has(consultor_id=consultor.id)).group_by(Agenda.data).all()

        # Construir o relatório
        relatorio = {
            "por_assunto": [
                {"assunto": r.assunto, "total": r.total} for r in relatorio_por_assunto
            ],
            "por_data": [
                {"data": str(r.data), "total": r.total} for r in relatorio_por_data
            ]
        }

        return JSONResponse(content={"relatorio": relatorio}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": "Erro ao gerar relatório de agendas.", "error": str(e)}, status_code=500)

    finally:
        session.close()
