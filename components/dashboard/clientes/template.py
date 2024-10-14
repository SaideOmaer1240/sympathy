from fasthtml.common import Titled, Div, P, H2, Button
from db.models import Cliente, Session
from starlette.responses import RedirectResponse

async def dashbord(req):
    email = req.state.user['sub']

    session = Session()
    cliente = session.query(Cliente).filter(Cliente.email == email).first()

    if not cliente:
        return RedirectResponse(url='/client', status_code=307)
    
    session.close()

    return Titled(
        'Área de Cliente',
        Div(
            H2(f"Bem-vindo, {cliente.nome}!", cls="text-2xl font-bold text-center text-indigo-700 my-4"),
            Div(
                # Card de informações rápidas
                Div(
                    P("Suas Consultas Agendadas", cls="text-gray-500"),
                    Button("Ver Consultas", cls="bg-blue-500 text-white px-4 py-2 rounded mt-2 hover:bg-blue-700"),
                    cls="bg-white shadow rounded-lg p-6 m-4"
                ),
                Div(
                    P("Avaliações Pendentes", cls="text-gray-500"),
                    Button("Ver Avaliações", cls="bg-green-500 text-white px-4 py-2 rounded mt-2 hover:bg-green-700"),
                    cls="bg-white shadow rounded-lg p-6 m-4"
                ),
                Div(
                    P("Notificações", cls="text-gray-500"),
                    Button("Ver Notificações", cls="bg-yellow-500 text-white px-4 py-2 rounded mt-2 hover:bg-yellow-700"),
                    cls="bg-white shadow rounded-lg p-6 m-4"
                ),
                cls="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4"
            ),
            cls="container mx-auto py-6"
        )
    )
