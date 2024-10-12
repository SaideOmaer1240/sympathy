from db.models import Pedido, Consultor, Agenda, Session
from fasthtml.common import Titled, Tr, Td, Button, Table, Thead, Tbody, Th, P
from starlette.responses import JSONResponse
from datetime import datetime, timezone

async def aceitar_pedido(req, pedido_id: int):
    session = Session()
    consultor_email = req.state.user["sub"]  # Email do consultor logado, extraído do token

    try:
        # Buscar o consultor logado
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        if not consultor:
            session.close()
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        # Buscar o pedido de consultoria
        pedido = session.query(Pedido).filter(Pedido.id == pedido_id, Pedido.consultor_id == consultor.id).first()
        if not pedido:
            session.close()
            return JSONResponse(content={"message": "Pedido não encontrado."}, status_code=404)

        # Atualizar o status do pedido para "aceito"
        pedido.status = "aceito"
        session.commit()

        # Criar uma agenda para esse pedido
        nova_agenda = Agenda(
            pedido_id=pedido.id, 
            assunto=f"Consulta com {pedido.cliente.nome}",  
            data=datetime.now(timezone.utc).date(),  
            horario=datetime.now(timezone.utc).time(),  
            created_at=datetime.now(timezone.utc),
        )
        session.add(nova_agenda)
        session.commit()

        return JSONResponse(content={"message": "Pedido aceito e agenda criada com sucesso!"}, status_code=200)

    except Exception as e:
        session.rollback()
        return JSONResponse(content={"message": f"Erro ao aceitar pedido: {str(e)}"}, status_code=500)
    
    finally:
        session.close()

async def listar_pedidos(req):
    session = Session()
    consultor_email = req.state.user["sub"]  # Email do consultor logado, extraído do token

    # Buscar o consultor logado
    consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
    if not consultor:
        session.close()
        return Titled("Erro", P("Consultor não encontrado."))

    # Buscar todos os pedidos pendentes para esse consultor
    pedidos = session.query(Pedido).filter(Pedido.consultor_id == consultor.id, Pedido.status == "pendente").all()
    
    if not pedidos:
        session.close()
        return Titled("Pedidos de Consultoria", P("Nenhum pedido pendente encontrado."))

    # Construir a tabela de pedidos com botões para aceitar ou recusar
    pedido_rows = [
        Tr(
            Td(f"Cliente: {p.cliente.nome}"),  # Nome do cliente
            Td(f"Data: {p.created_at}"),  # Data do pedido
            Td(Button("Aceitar", onclick=f"window.location.href='/aceitar_pedido/{p.id}'")),
            Td(Button("Recusar", onclick=f"window.location.href='/recusar_pedido/{p.id}'"))
        ) for p in pedidos
    ]

    session.close()

    return Titled("Pedidos de Consultoria",
        Table(
            Thead(
                Tr(Th("Cliente"), Th("Data"), Th("Aceitar"), Th("Recusar"))
            ),
            Tbody(*pedido_rows)
        )
    )


async def recusar_pedido(req, pedido_id: int):
    session = Session()
    consultor_email = req.state.user["sub"]  # Email do consultor logado, extraído do token

    try:
        # Buscar o consultor logado
        consultor = session.query(Consultor).filter(Consultor.email == consultor_email).first()
        if not consultor:
            session.close()
            return JSONResponse(content={"message": "Consultor não encontrado."}, status_code=404)

        # Buscar o pedido de consultoria
        pedido = session.query(Pedido).filter(Pedido.id == pedido_id, Pedido.consultor_id == consultor.id).first()
        if not pedido:
            session.close()
            return JSONResponse(content={"message": "Pedido não encontrado."}, status_code=404)

        # Atualizar o status do pedido para "recusado"
        pedido.status = "recusado"
        session.commit()

        return JSONResponse(content={"message": "Pedido recusado com sucesso!"}, status_code=200)

    except Exception as e:
        session.rollback()
        return JSONResponse(content={"message": f"Erro ao recusar pedido: {str(e)}"}, status_code=500)
    
    finally:
        session.close()
