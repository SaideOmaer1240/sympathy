from fasthtml.common import Body, Div, Section, A, Button, I, Span, Ul, Li, H3, P, Script
from app.views import contar_agendas_livres, contar_agendas_ocupadas, contar_clientes_atendidos, contar_pedidos_pendentes, obter_agendas_recentes
from auth.decorators.authorization import autenticar

@autenticar('consultor')
async def dashboard(req):
    # Obtenção de dados
    agendas_ocupadas = await contar_agendas_ocupadas(req)
    agendas_livres = await contar_agendas_livres(req)
    clientes_atendidos = await contar_clientes_atendidos(req)
    pedidos_consulta = await contar_pedidos_pendentes(req)
    agendas_recentes = await obter_agendas_recentes(req)

    return Body(
        Section(
            # Sidebar
            Div(
                Div(
                    A("Sympathy", href="#", cls="text-2xl font-bold m-4"),
                    cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",
                ),
                Ul(
                    Li(
                        A(
                            I(cls="fas fa-calendar-plus mr-2"), 
                            Span("Criar Agenda", cls="menu-text"),
                            hx_get="/form_criar_agenda",
                            hx_target="#main-content",
                            hx_swap="innerHTML",
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    Li(
                        A(
                            I(cls="fas fa-calendar-check mr-2"), 
                            Span("Agendas Ocupadas", cls="menu-text"),
                            hx_get="/minhas_agendas?ocupadas=true",
                            hx_target="#main-content",
                            hx_swap="innerHTML",
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    Li(
                        A(
                            I(cls="fas fa-user-md mr-2"), 
                            Span("Pedidos de Consulta", cls="menu-text"),
                            hx_get="/listar_pedidos_consulta",
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
            
            # Área Principal
            Div(
                Div(
                    A("Painel de Consultor", href="#", cls="text-2xl font-bold m-4 items-end"),
                    Button("☰", cls="text-white m-4 text-3xl md:hidden", onclick="toggleSidebar()", id="menu-toggle"),
                    cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",
                ),
                
                # Seção de Estatísticas
                Div(
                    Div(
                        P("Agendas Ocupadas", cls="text-gray-500"),
                        H3(str(agendas_ocupadas), cls="text-3xl font-bold text-gray-900"),
                        cls="p-6 bg-white shadow rounded-lg"
                    ),
                    Div(
                        P("Agendas Livres", cls="text-gray-500"),
                        H3(str(agendas_livres), cls="text-3xl font-bold text-gray-900"),
                        cls="p-6 bg-white shadow rounded-lg"
                    ),
                    Div(
                        P("Clientes Atendidos", cls="text-gray-500"),
                        H3(str(clientes_atendidos), cls="text-3xl font-bold text-gray-900"),
                        cls="p-6 bg-white shadow rounded-lg"
                    ),
                    Div(
                        P("Pedidos de Consulta Pendentes", cls="text-gray-500"),
                        H3(str(pedidos_consulta), cls="text-3xl font-bold text-gray-900"),
                        cls="p-6 bg-white shadow rounded-lg"
                    ),
                    cls="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4",
                    id="cards-section"
                ),
                
                # Seção de Agendas Recentes com botão de alternância
                Div(
                    Button('▼ Agendas Recentes', cls='text-2xl ml-10 font-bold text-purple-700 mb-4', id='toggle-button', onclick="toggleCardsSection()"),
                    Div(
                        *[
                            Div(
                                P(f"Data: {agenda['data']}", cls="text-gray-500"),
                                P(f"Horário: {agenda['horario']}", cls="text-gray-700"),
                                P(f"Cliente: {agenda['cliente']}", cls="text-gray-700"),
                                Button("Ver Detalhes", hx_get=f"/detalhes_agenda/{agenda['id']}", hx_target="#main-content", hx_swap="innerHTML", cls="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded mt-2"),
                                cls="p-4 bg-white shadow-md rounded-lg mb-4"
                            ) for agenda in agendas_recentes
                        ],
                        cls="px-8 py-4 overflow-auto",
                        style="height: 20rem",
                        id="agenda-list"
                    )
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
