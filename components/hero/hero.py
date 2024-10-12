from fasthtml.common import Div, H1, I, H3,  P, Button, Span, Ul, Li, A,  H2, H3, Nav, Ul, Li, P, A, Form, Input, Button, Script

# Navbar
def Navbar():
    return Nav(
         Div(
               Div(
                    A("Sympathy", href="#", cls="text-2xl font-bold m-4"),
                     
                    cls="flex justify-between items-center w-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white",),
                
                Ul(
                    Li(
                        A(
                            I(cls="fas fa-lightbulb mr-2"),  # Ícone de ideia adicionado
                            Span("Home", cls="menu-text"), 
                            hx_get="/", hx_target='#body', hx_swap='outerHTML', 
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    Li(
                        A(
                            I(cls="fas fa-lightbulb mr-2"),  # Ícone de ideia adicionado
                            Span("Login", cls="menu-text"), 
                            hx_get="/form_login", hx_target='#hero', hx_swap='outerHTML', 
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    Li(
                        A(
                            I(cls="fas fa-lightbulb mr-2"),  # Ícone de ideia adicionado
                            Span("Cadastre-se como Consultor", cls="menu-text"), 
                            hx_get="/form_cadastrar_consultor", hx_target='#hero', hx_swap='outerHTML', 
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ),
                    Li(
                        A(
                            I(cls="fas fa-lightbulb mr-2"),  # Ícone de ideia adicionado
                            Span("Cadastre-se como cliente", cls="menu-text"), 
                            hx_get="/form_cadastrar_cliente", hx_target='#hero', hx_swap='outerHTML', 
                            cls="sidebar-link flex items-center p-2 text-white hover:bg-purple-600"
                        )
                    ), 
                    cls="space-y-4", id="sidebar-menu"
                ),
                cls="sidebar fixed top-0 md:hidden md:top-auto left-0 w-64 h-full bg-gradient-to-l from-purple-900 to-indigo-800 text-white transition-transform transform -translate-x-full md:translate-x-0", id="sidebar"
            ),

   
        Div(
            Div(
                A("Sympathy", href="#", cls="text-2xl font-bold text-white"),
                
                # Ícone do menu para dispositivos móveis
                A("☰", href="#", cls="text-white text-3xl md:hidden", onclick="toggleSidebar()", id="menu-toggle"),

                # Menu completo, oculto em telas menores e mostrado em telas grandes
                Ul(
                    Li(A("Home", hx_get="/", hx_target='#body', hx_swap='outerHTML', cls="text-gray-300 hover:text-white hover:shadow-md transition duration-300")),
                    Li(A("Consultores", href="#", cls="text-gray-300 hover:text-white hover:shadow-md transition duration-300")),
                    Li(A("Login", hx_get="/form_login", hx_target='#hero', hx_swap='outerHTML', cls="text-gray-300 hover:text-white hover:shadow-md transition duration-300")),
                    Li(A("Contato", href="#", cls="text-gray-300 hover:text-red hover:shadow-md transition duration-300")),
                    cls="hidden md:flex space-x-6 pr-10"  # Oculto em telas pequenas (md:hidden), mostrado em médias ou maiores (md:flex)
            ),


                cls="flex justify-between items-center w-full"
            ),
            cls="bg-blue-900 py-6 px-8 shadow-lg w-full"
        ), 
        cls='w-full fixed top-0 z-10'
    )

# Hero Section
def HeroSection():
    return Div(
        Div(
            H1("Encontre os Melhores Consultores para Suas Necessidades", 
               cls="text-5xl font-bold text-white mb-4 animate-fade-in lg:mr-20 md:mr-10 sm:mr-4"),
            P("Plataforma que conecta clientes a profissionais qualificados.",
              cls="text-lg text-gray-300 mb-8"),
            Div(
                A("Cadastre-se como Consultor", hx_get="/form_cadastrar_consultor", hx_target='#hero', hx_swap='outerHTML',  
                cls="bg-white text-indigo-600 px-6 py-3 rounded-full font-semibold hover:bg-gray-200 transition duration-300"),
                A("Encontre um Consultor", hx_get="/form_cadastrar_cliente", 
                 hx_target='#hero', hx_swap='outerHTML',   cls="ml-4 bg-indigo-500 text-white px-6 py-3 rounded-full font-semibold hover:bg-indigo-700 transition duration-300"),
                cls="flex justify-center space-x-4"
            ),
            cls="text-center"
        ),
        Script(src='static/js/toggle/agendasRecents.js'),
        Script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"),
        Script(src='static/js/toggle/toggleSidebar.js' ),

        cls="bg-gradient-to-r from-gray-900 to-indigo-800 h-screen flex items-center justify-center w-full", id='hero',  
    )

# Cards Section
def CardsSection():
    cards = [
        {"title": "Consultoria de TI", "description": "Especialistas em tecnologia para otimizar seu negócio."},
        {"title": "Consultoria Financeira", "description": "Gerenciamento financeiro e contabilidade."},
        {"title": "Consultoria em Marketing", "description": "Estrategistas para aumentar sua presença no mercado."}
    ]
    
    return Div(
        H2("Nossos Consultores", cls="text-3xl font-bold text-center my-10 text-gray-800"),
        Div(
            *[Card(card["title"], card["description"]) for card in cards],
            cls="flex flex-wrap justify-center space-x-4 space-y-6 md:space-y-0 md:space-x-8"  # Ajustes no espaçamento e flex-wrap
        ),
        cls="py-16 bg-gray-100"
    )

def Card(title, description):
    return Div(
        Div(
            H3(title, cls="text-xl font-semibold mb-4"),
            P(description, cls="text-gray-700 mb-4"),
            A("Saiba Mais", href="#", cls="text-indigo-600 font-semibold hover:underline"),
            cls="p-6 bg-white rounded-lg shadow-lg hover:shadow-2xl transition-transform transform hover:scale-105 hover:bg-gray-50"
        ),
        cls="w-full sm:w-1/2 md:w-1/3 lg:w-1/4 mb-6"  # Classes responsivas para definir colunas
    )

# Footer
def Footer():
    return Div(
        P("© 2024 Plataforma de Consultores. Todos os direitos reservados.",
          cls="text-center text-gray-600 py-4"),
        cls="bg-gray-900"
    )

def buscar_consultores_div():
    return Div(
            Form(
                Div(
                    Input(type="text", name="area_atuacao", placeholder="Área de Atuação", cls="border p-2 mb-4"),
                    Button("Buscar", type="submit", cls="bg-blue-500 text-white p-2 rounded"),
                    cls="flex flex-col"
                ),
                method="POST"
            ),
            cls="flex justify-center items-center h-screen bg-gray-100"
        )
