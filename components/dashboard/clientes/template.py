from fasthtml.common import Body, Div, Section, A, Button, I, Span, Ul, Li, H3, P, Form, Input, Label, Script
from app.viewsClients import buscar_consultores_cliente, listar_historico_consultas_cliente, get_client_info
from auth.decorators.authorization import autenticar

@autenticar('cliente')
async def dashboard_cliente(req):
    # Obtenção de dados
    consultores_disponiveis = await buscar_consultores_cliente(req)   
    historico_consultas = await listar_historico_consultas_cliente(req)
    cliente = await get_client_info(req)

    return Body(
        Section(
            # Sidebar para o cliente
            Div(
                Div(
                    A("Sympathy", href="#", cls="text-2xl font-bold m-4"),
                    cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",
                ),
                Ul(
                    Li(
                        A(
                            I(cls="fas fa-search mr-2"), 
                            Span("Buscar Consultores", cls="menu-text"),
                            hx_get="/buscar_consultores_cliente",
                            hx_target="#main-content",
                            hx_swap="innerHTML",
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    Li(
                        A(
                            I(cls="fas fa-history mr-2"), 
                            Span("Histórico de Consultas", cls="menu-text"),
                            hx_get="/listar_historico_consultas_cliente",
                            hx_target="#main-content",
                            hx_swap="innerHTML",
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    cls="space-y-4",
                    id="sidebar-menu"
                ),
                cls="sidebar fixed top-0 md:relative md:top-auto left-0 w-64 h-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white transition-transform transform -translate-x-full md:translate-x-0",
                id="sidebar"
            ),
            
            # Área Principal do Dashboard do Cliente
            Div(
                Div(
                    P(cliente.nome, cls="text-base font-bold m-4 items-end"),
                    A("Painel do Cliente", href="#", cls="text-2xl font-bold m-4 items-end"),
                    Button("☰", cls="text-white m-4 text-3xl md:hidden", onclick="toggleSidebar()", id="menu-toggle"),
                    cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",
                ),
                
                # Formulário de Pesquisa de Consultores
                Div(
                    H3("Buscar Consultores", cls="text-2xl ml-10 font-bold text-purple-700 mb-4"),
                    Form(
                        Div(
                            Label("Nome ou Área de Atuação:", cls="block text-gray-700 font-bold"),
                            Input(type="text", name="termo", placeholder="Digite o nome ou área de atuação", cls="w-full p-2 mb-4 border rounded"),
                            Label("Avaliação Mínima:", cls="block text-gray-700 font-bold"),
                            Input(type="number", name="avaliacao_minima", placeholder="1 a 5", min="1", max="5", step="0.1", cls="w-full p-2 mb-4 border rounded"),
                            Label("Apenas Disponíveis:", cls="block text-gray-700 font-bold"),
                            Input(type="checkbox", name="apenas_disponiveis", cls="mb-4"),
                            Button("Buscar", type="submit", cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded", hx_post="/buscar_consultores",  hx_target="#cards-section",  hx_trigger="click", hx_swap="outerHTML"   ),  method="POST", action="/buscar_consultores", cls="p-6 bg-white shadow rounded-lg"
                    )),
                    Div(
                        consultores_disponiveis, cls="mt-4"
                    ), id='cards-section'
                ),
                
                # Seção de Histórico de Consultas
                Div(
                    Button('▼ Histórico de Consultas', cls='text-2xl ml-10 font-bold text-purple-700 mb-4', id='toggle-button', onclick="toggleCardsSection()"),
                    Div(
                        *[
                            Div(
                                P(f"Data: {consulta['data']}", cls="text-gray-500"),
                                P(f"Consultor: {consulta['consultor']}", cls="text-gray-700"),
                                P(f"Status: {consulta['status']}", cls="text-gray-700"),
                                cls="p-4 bg-white shadow-md rounded-lg mb-4"
                            ) for consulta in historico_consultas
                        ],
                        cls="px-8 py-4 overflow-auto",
                        style="height: 20rem",
                        id="agenda-list"
                    ),
                ),
                cls="w-full main bg-gray-100",
                id="main"
            ),
            cls="flex fixed flex-col md:h-full md:flex-row w-full top-0"
        ),
        Script(src='static/js/toggle/agendasRecents.js'),
        Script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"),
        Script(src='static/js/toggle/toggleSidebar.js')
    )
