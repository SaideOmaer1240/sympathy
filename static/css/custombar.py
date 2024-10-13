from fasthtml.common import Html, Body, Div, H1, H2, H3, H5, P, Button, Nav, Ul, Li, A, Textarea, Section, Form, Input, Script  
 
def dashboard(consultor):
    return Body(
        Script(src='static/js/toggle/agendasRecents.js'),
        
        Section(
            # Sidebar
            Div(
                Div(
                    H2("Sympathy", cls=" md:sidebar-hidden text-2xl font-bold text-white mb-8"),
                     Button("☰", cls="text-white text-3xl md:hidden p-4 menu-icon"), 
                    
                      cls="flex items-center space-x-4 px-8 py-4 border-b bg-gradient-to-l from-purple-900 to-indigo-800 text-white"),
                Nav(
                    Ul(
                        Li(A("Criar Agenda", href="#", cls="flex items-center p-2 text-white hover:bg-purple-600")),
                        Li(A("Ver Agendas Ocupadas", href="#", cls="flex items-center p-2 text-white hover:bg-purple-600")),
                        Li(A("Ver Agendas Livres", href="#", cls="flex items-center p-2 text-white hover:bg-purple-600")),
                        Li(A("Clientes Atendidos", href="#", cls="flex items-center p-2 text-white hover:bg-purple-600")),
                        Li(A("Clientes Não Atendidos", href="#", cls="flex items-center p-2 text-white hover:bg-purple-600")),
                        Li(A("Pedidos de Consulta", href="#", cls="flex items-center p-2 text-white hover:bg-purple-600")),
                        cls="space-y-4 flex flex-col"
                    ),
                    cls="mt-10 mr-0 h-screen overflow-y-auto",
                ),
                cls="p-4 bg-purple-800 esconder-no-movel",  
                id="sidebar"
            ),

           
           
            # Main Content Area
            Div(
                # Header Section
                
                   
                         # Custom class for menu icon
                        Div(
                            Button("☰", cls="text-white text-3xl md:hidden p-4 menu-icon"), 
                            H5("Painel de Consultor", cls="font-bold text-white mb-2 text-2xl"), cls="flex items-center space-x-4 px-8 py-4 border-b bg-gradient-to-l from-purple-900 to-indigo-800 text-white"),

                        
                     
               

                # Cards Section
                Div(
                    Div(
                        Div(
                            P("Agendas Ocupadas", cls="text-gray-500"),
                            H3("12", cls="text-3xl font-bold text-gray-900"),
                            cls="p-6 bg-white shadow rounded-lg"
                        ),
                        Div(
                            P("Agendas Livres", cls="text-gray-500"),
                            H3("8", cls="text-3xl font-bold text-gray-900"),
                            cls="p-6 bg-white shadow rounded-lg"
                        ),
                        Div(
                            P("Clientes Atendidos", cls="text-gray-500"),
                            H3("20", cls="text-3xl font-bold text-gray-900"),
                            cls="p-6 bg-white shadow rounded-lg"
                        ),
                        Div(
                            P("Pedidos de Consulta", cls="text-gray-500"),
                            H3("5", cls="text-3xl font-bold text-gray-900"),
                            cls="p-6 bg-white shadow rounded-lg"
                        ),
                        cls="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4"  # Responsividade implementada
                    ),
                    cls="p-8",
                    id="cards-section"  # ID para referência
                ),

                Div(
                    Button('▲ Agendas Recentes', cls='text-2xl ml-10 font-bold text-gray-700 mb-4', id='toggle-button', onclick="toggleCardsSection()"),   Div(
                        Div(
                            Div(
                                P("Data: 02/10/2024", cls="text-gray-500"),
                                P("Horário: 14h00 - 15h00", cls="text-gray-700"),
                                P("Cliente: João Silva", cls="text-gray-700"),
                                Button("Ver Detalhes", cls="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded mt-2"),
                                cls="p-4 bg-white shadow-md rounded-lg mb-4"
                            ),
                            Div(
                                P("Data: 02/10/2024", cls="text-gray-500"),
                                P("Horário: 16h00 - 17h00", cls="text-gray-700"),
                                P("Cliente: Maria Santos", cls="text-gray-700"),
                                Button("Ver Detalhes", cls="text-white bg-blue-500 hover:bg-blue-700 px-4 py-2 rounded mt-2"),
                                cls="p-4 bg-white shadow-md rounded-lg mb-4"
                            ),
                            cls="space-y-4 mb-80 agenda-list"  # Custom class for list
                        ),
                        cls="px-8 py-4 overflow-auto", style='height: 20rem', id='agenda-list'
                    ),
                ),  # Agenda List Section
                
                cls="w-full main bg-gray-100"
            ),
            cls="flex fixed flex-col md:flex-row w-full top-0",
        ),

        cls="flex flex-col md:flex-row w-full top-0",
    )
# Página para o consultor criar uma agenda
def agenda_page():
    return Div(
        H1("Criar Agenda"),
        Form(
            Input(type="datetime-local", name="data_hora", placeholder="Data e Hora", cls="border p-2 mb-4"),
            Input(type="number", name="duracao", placeholder="Duração (minutos)", cls="border p-2 mb-4"),
            Textarea(name="descricao", placeholder="Descrição do compromisso", cls="border p-2 mb-4"),
            Button("Criar Agenda", type="submit", cls="bg-blue-500 text-white p-2 rounded"),
            method="POST", action="/inserir-agenda"
        ),
        cls="container mt-5"
    )

