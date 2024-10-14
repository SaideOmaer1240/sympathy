from fasthtml.common import *
from auth.decorators.authorization import autenticar
from db.models import init_db
from app.views import atualizar_agenda, cadastrar_cliente, cadastrar_consultor, criar_agenda, eliminar_agenda, minhas_agendas, template_editar_agenda, login, buscar_agendas_por_assunto, duplicar_agenda, listar_agendas_concluidas, gerar_relatorio_agendas
from app.view_pedidos import aceitar_pedido, listar_pedidos, recusar_pedido
from app.templates.forms import template_agenda, template_cliente,template_consultor, template_login, template_buscar_agenda, template_buscar_consultores
from components.hero.template import HeroSection, CardsSection, Navbar
from app.viewsClients import buscar_consultores, detalhes_consultor, fazer_pedido_consulta
from components.dashboard.consultores.template import dashboard
from components.dashboard.clientes.template import dashbord as area_client
from components.head.template import head
from components.login import conectar
from components.exceptions.message import notice

# Criar todas as tabelas no banco de dados
init_db()

# Inicialização do aplicativo FastHTML
app, rt = fast_app()

# Página inicial
@app.get("/")
async def homepage():
    return Html( 
        head(),
        
    Body(
        Div(
        
        # Navbar
        Navbar(),
        
        # Hero Section
        HeroSection(),
        
        # Cards Section
        CardsSection(),
        
        # Footer
        Footer(),
        cls='w-full bg-gradient-to-r from-gray-900 to-indigo-800 h-screen'
    ), id='body', cls='max-h-screen'

        )
        , 
)


# Formulário de Cadastro de Consultor (Front-End)
@rt("/form_cadastrar_consultor")
def form_cadastrar_consultor():
    return template_consultor()

# Rota para Cadastro de Consultor  (Back-End)
@rt("/cadastrar_consultor", methods=["POST"])
async def route_consultor(req):
    return await cadastrar_consultor(req)   

# Formulário de Cadastro de Cliente (Front-End)
@rt("/form_cadastrar_cliente")
def form_cadastrar_cliente():
    return template_cliente()

# Rota para Cadastro de Cliente (Back-End)
@rt("/cadastrar_cliente", methods=["POST"])
async def rota_cliente(req):
    return await cadastrar_cliente(req)

# Formulário de Login (Front-End)
@rt("/form_login")
def form_login():
    return template_login()

# Função de login para consultores e clientes (Back-End)
@rt("/login", methods=["POST"])
async def route_login(req):
     return await login(req)

# Função para redirecionar consultor pre-logado
@rt("/connected_as_a_consultant") 
async def consultor_logado(req):
    return await dashboard(req)

# Função para redirecionar o usuario para login apos o cadastro
@rt("/consultant")
async def connect():
    return conectar()

# Função para redirecionar o usuario para login apos o cadastro
@rt("/client")
@autenticar(role='cliente')
async def connect(req):
    return await area_client(req)

# Rota para apresentar mensagem caso o email já foi usado
@rt('/exist')
async def exit_email_con():
    return notice(msg='Email já cadastrado.', url1='/consultant', actionName1='Conectar-se como consultor', url2='/client',actionName2='Conectar-se como cliente')

# Função de dashboard para consultores 
@rt("/dashboard_consultor")
@autenticar(role='consultor')
async def dashboards(req):
    return await dashboard(req)

# Função de dashboard para clientes 
@rt("/dashboard_cliente")
@autenticar(role='cliente')
async def cliente(req):
    return await area_client(req)


# Formulário para Criar Agenda (Front-End)
@rt("/form_criar_agenda")
def form_criar_agenda():
    return template_agenda()

# Rota para Criar Agenda (Back-End)
@rt("/criar_agenda", methods=["POST"])
@autenticar(role='consultor')
async def rota_criar_agenda(req): 
     return await criar_agenda(req)

# Rota para listar as agendas do consultor logado e retornar em HTML
@rt("/minhas_agendas", methods=["GET"])
@autenticar(role='consultor')
async def rota_agendas(req):
     return await minhas_agendas(req)

# Formulário para buscar agendas
@rt("/form_buscar_agenda")
@autenticar(role='consultor')  # Apenas consultores podem buscar agendas
def form_buscar_agenda():
    return template_buscar_agenda()

# Função backend para processar a busca
@rt("/buscar_agenda_por_assunto", methods=["POST"])
@autenticar(role='consultor')
async def rota_buscar_agenda(req):
    return await buscar_agendas_por_assunto(req)



# Rota para eliminar uma agenda do consultor logado 
@rt("/eliminar_agenda/{agenda_id}", methods=["POST"]) 
@autenticar(role="consultor")
async def rota_eliminar_agenda(req, agenda_id: int):
    return await eliminar_agenda(req, agenda_id)

# Rota para atualizar uma agenda do consultor logado
@rt("/atualizar_agenda/{agenda_id}", methods=["POST"]) 
@autenticar(role='consultor')
async def rota_atualizar_agenda(req, agenda_id: int):
   return await atualizar_agenda(req, agenda_id)

# Formulário para Editar Agenda
@rt("/form_editar_agenda/{agenda_id}")
@autenticar(role='consultor')
async def form_editar_agenda(req, agenda_id: int):
   return await template_editar_agenda(req, agenda_id)

# Rota para duplicar uma agenda do consultor logado
@rt("/duplicar_agenda/{agenda_id}", methods=["POST"])
@autenticar(role='consultor')
async def rota_duplicar_agenda(req, agenda_id: int):
    return await duplicar_agenda(req, agenda_id)

 # Rota para listar agendas concluídas do consultor logado
@rt("/historico_agendas", methods=["GET"])
@autenticar(role='consultor')
async def rota_historico_agendas(req):
    return await listar_agendas_concluidas(req)


# Rota para gerar o relatório de agendas do consultor logado
@rt("/relatorio_agendas", methods=["GET"])
@autenticar(role='consultor')
async def rota_relatorio_agendas(req):
    return await gerar_relatorio_agendas(req)

# Rota HTMX para buscar consultores
@rt("/buscar_consultores", methods=["POST"])
@autenticar(role='cliente')  # Apenas clientes podem buscar consultores
async def rota_buscar_consultores(req):
    return await buscar_consultores(req)

# Rota HTMX para ver detalhes de consultor
@rt("/detalhes_consultor/{consultor_id}", methods=["GET"])
@autenticar(role='cliente')  # Apenas clientes podem visualizar detalhes
async def rota_detalhes_consultor(req, consultor_id: int):
    return await detalhes_consultor(req, consultor_id)

# Rota HTMX para fazer pedido de consultoria
@rt("/fazer_pedido_consulta/{consultor_id}", methods=["POST"])
@autenticar(role='cliente')  # Apenas clientes podem fazer pedidos de consultoria
async def rota_fazer_pedido(req, consultor_id : int):
    return await fazer_pedido_consulta(req, consultor_id)
 
# Rota que exibe o formulário de busca de consultores (Frontend)
@rt("/form_buscar_consultores")
@autenticar(role='cliente')  # Apenas clientes podem buscar consultores
async def form_buscar_consultores(req):  # Adicione o parâmetro 'req'
    return template_buscar_consultores()

# Rota para listar pedidos pendentes
@rt("/listar_pedidos", methods=["GET"])
@autenticar(role='consultor')
async def rota_listar_pedidos(req):
    return await listar_pedidos(req)

# Rota para aceitar um pedido
@rt("/aceitar_pedido/{pedido_id}", methods=["GET"])
@autenticar(role='consultor')
async def rota_aceitar_pedido(req, pedido_id: int):
    return await aceitar_pedido(req, pedido_id)

# Rota para recusar um pedido
@rt("/recusar_pedido/{pedido_id}", methods=["GET"])
@autenticar(role='consultor')
async def rota_recusar_pedido(req, pedido_id: int):
    return await recusar_pedido(req, pedido_id)

serve()