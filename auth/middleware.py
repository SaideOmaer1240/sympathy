home/saide/sympathy/components/dashboard/consultores/template.py
    from fasthtml.common import Body, Div, H1, I, H3, H5, P, Button, Span, Ul, Li, A, Textarea, Section,   Script

    async def dashboard(req):
        # Logica


        # Retornar resultados
        return Body(
            Section(
                # Sidebar
                Div(
                Div(
                        A("Sympathy", href="#", cls="text-2xl font-bold m-4"),
                        
                        cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",),
                    
                    Ul(
                        Li(
                            A(
                                I(cls="fas fa-calendar-plus mr-2"), 
                                Span("Criar Agenda", cls="menu-text"), 
                                href="#", 
                                cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                            )
                        ),
                        Li(
                            A(
                                I(cls="fas fa-calendar-check mr-2"), 
                                Span("Ver Agendas Ocupadas", cls="menu-text"), 
                                href="#", 
                                cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                            )
                        ),
                        Li(
                            A(
                                I(cls="fas fa-calendar-alt mr-2"), 
                                Span("Ver Agendas Livres", cls="menu-text"), 
                                href="#", 
                                cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                            )
                        ),
                        Li(
                            A(
                                I(cls="fas fa-user-check mr-2"), 
                                Span("Clientes Atendidos", cls="menu-text"), 
                                href="#", 
                                cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                            )
                        ),
                        Li(
                            A(
                                I(cls="fas fa-user-times mr-2"), 
                                Span("Clientes Não Atendidos", cls="menu-text"), 
                                href="#", 
                                cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                            )
                        ),
                        Li(
                            A(
                                I(cls="fas fa-user-md mr-2"), 
                                Span("Pedidos de Consulta", cls="menu-text"), 
                                href="#", 
                                cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                            )
                        ),
                        cls="space-y-4", id="sidebar-menu"
                        ),
                    
                    cls="sidebar fixed top-0 md:relative md:top-auto left-0 w-64 h-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white transition-transform transform -translate-x-full md:translate-x-0", id="sidebar"
                ),

                # Main Content Area      
                Div(
                    Div(
                        A(),
                        A("Painel de Consultor", href="#", cls="text-2xl font-bold m-4 items-end"),
                        
                        # Ícone do menu para dispositivos móveis
                        Button("☰", cls="text-white m-4 text-3xl md:hidden", onclick="toggleSidebar()", id="menu-toggle"),
                        cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",),

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
                            cls="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4"
                        ),
                        cls="p-8",
                        id="cards-section"
                    ),
                    
                    Div(
                        Button('▼ Agendas Recentes', cls='text-2xl ml-10 font-bold text-purple-700 mb-4', id='toggle-button', onclick="toggleCardsSection()"),
                        Div(
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
                                cls="space-y-4 agenda-list"
                            ),
                            cls="px-8 py-4 overflow-auto", style='height: 20rem', id='agenda-list'
                        ),
                    ),
                    cls="w-full main bg-gray-100", id='main'
                ),
                cls="flex fixed flex-col md:h-full md:flex-row w-full top-0",
            ),
            Script(src='static/js/toggle/agendasRecents.js'),
            Script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"),
            Script(src='static/js/toggle/toggleSidebar.js' ),
            cls="flex flex-col md:flex-row w-full top-0",
        ) 

