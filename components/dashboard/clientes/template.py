from fasthtml.common import Titled, Div, P
from db.models import Session, Cliente
from starlette.responses import RedirectResponse

async def dashbord(req):
    # Logica
    email = req.state.user['sub']

    # Buscar cliente logado
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.email == email).first()

    if not cliente:
        return RedirectResponse(url='/client', status_code=307)
    session.close()

    # Retornar resposta
    return Titled(
        'Area de cliente',
        Div(
            P(f"Bem-vindo, Cliente {cliente.nome}!")
        )
    )