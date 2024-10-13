from fasthtml.common import Titled, Fieldset, Form, Label, Input, Button, Tr, Td, Table, Thead, Tbody, Tr, Th, Td, Div, P, H1, A , Span

def template_cliente():
    return Div(
        H1("Cadastro de Clientes", cls="text-3xl font-bold text-center mb-6"),
        Form(
            Div(
                Label("Nome: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="text", name="nome", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-green-500"),
                cls="mb-4"
            ),
            Div(
                Label("Email: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="email", name="email", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-green-500"),
                cls="mb-4"
            ),
            Div(
                Label("Senha: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="password", name="senha", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-green-500"),
                cls="mb-4"
            ),
            Button("Cadastrar", type="submit", cls="bg-green-500 text-white py-3 px-6 rounded-full hover:bg-green-600 transition-all duration-300"),
            method="POST", action="/cadastrar_cliente", cls="space-y-4"
        ),
        Div(
            P("Possui uma conta?", cls="text-center mt-4"),
            Div(
                A("Login", hx_get="/form_login", hx_target='#forms', hx_swap='#outerHTML', cls="text-green-500 hover:underline mx-2"),
                Span("|", cls="mx-2"),
                A("Cadastre-se como Consultor", hx_get="/form_cadastrar_consultor", hx_target='#forms', hx_swap='outerHTML', cls="text-green-500 hover:underline mx-2"),
                cls="text-center"
            ),
            cls="mt-6"
        ),
        cls="container mx-auto max-w-lg mt-20 p-6 bg-white shadow-md rounded-lg", id='forms'
    )

def template_consultor():
    return Div(
        H1("Cadastro de Consultores", cls="text-3xl font-bold text-center mb-6"),
        Form(
            Div(
                Label("Nome: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="text", name="nome", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"),
                cls="mb-4"
            ),
            Div(
                Label("Email: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="email", name="email", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"),
                cls="mb-4"
            ),
            Div(
                Label("Área de Atuação: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="text", name="atuacao", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"),
                cls="mb-4"
            ),
            Div(
                Label("Senha: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="password", name="senha", required=True, cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"),
                cls="mb-4"
            ),
            Button("Cadastrar", type="submit", cls="bg-blue-500 text-white py-3 px-6 rounded-full hover:bg-blue-600 transition-all duration-300"),
            method="POST", action="/cadastrar_consultor", cls="space-y-4"
        ),
        Div(
            P("Possui uma conta?", cls="text-center mt-4"),
            Div(
                A("Login", hx_get="/form_login", hx_target='#forms', hx_swap='outerHTML', cls="text-blue-500 hover:underline mx-2"),
                Span("|", cls="mx-2"),
                A("Cadastre-se como Cliente", hx_get="/form_cadastrar_cliente", hx_target='#forms', hx_swap='outerHTML', cls="text-blue-500 hover:underline mx-2"),
                cls="text-center"
            ),
            cls="mt-6"
        ),
        cls="container mx-auto max-w-lg mt-20 p-6 bg-white shadow-md rounded-lg", id='forms'
    )

def template_buscar_consultores():
        return Titled("Buscar Consultores",
            Form(method="post", action="/buscar_consultores", hx_post="/buscar_consultores", hx_target="#lista-consultores")(
                Fieldset(
                    Label("Nome ou Área de Atuação: ", Input(name="termo", type="text", required=True)),
                    Label("Avaliação Mínima: ", Input(name="avaliacao_minima", type="number", step="0.1", min="1", max="5")),
                    Label("Apenas Disponíveis: ", Input(name="apenas_disponiveis", type="checkbox"))
                ),
                Button("Buscar", type="submit")
            ),
            Div(id="lista-consultores", style="margin-top: 20px;")(),  # Onde a lista de consultores será renderizada
            Div(id="detalhes-consultor", style="display:none; margin-top: 20px;")(
                P("Nome: ", id="consultor-nome"),
                P("Área de Atuação: ", id="consultor-atuacao"),
                Button("Solicitar Consultoria", id="btn-solicitar", hx_post="/fazer_pedido_consulta", hx_trigger="click", hx_vals="{consultor_id: consultorId}")
            )
        )
def template_login():
    return Div(
        H1("Login", cls="text-3xl font-bold text-center mb-6"),
        Form(
            Div(
                Label("Email: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="email", name="email", required=True, placeholder="Email", cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"),
                cls="mb-4"
            ),
            Div(
                Label("Senha: ", cls="block text-sm font-medium text-gray-700"),
                Input(type="password", name="senha", required=True, placeholder="Senha", cls="border border-gray-300 p-3 rounded w-full mb-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"),
                cls="mb-4"
            ),
            Button("Entrar", type="submit", cls="bg-indigo-500 text-white py-3 px-6 rounded-full hover:bg-indigo-600 transition-all duration-300"),
            method="POST", action="/login", hx_post='/login', hx_target='#body', hx_swap='outerHTML', cls="space-y-4"
        ),
        Div(
            P("Não possui uma conta?", cls="text-center mt-4"),
            Div(
                A("Cadastre-se como Consultor", hx_get="/form_cadastrar_consultor", hx_target='#forms', hx_swap='outerHTML', cls="text-indigo-500 hover:underline mx-2"),
                Span("|", cls="mx-2"),
                A("Cadastre-se como Cliente", hx_get="/form_cadastrar_cliente", hx_target='#forms', hx_swap='outerHTML', cls="text-indigo-500 hover:underline mx-2"),
                cls="text-center"
            ),
            cls="mt-6"
        ),
        cls="container mx-auto max-w-lg mt-20 p-6 bg-white shadow-md rounded-lg", id='forms'
    )

def template_agenda():
    return Titled("Criar Agenda",
        Form(method="post", action="/criar_agenda")(
            Fieldset(
                Label("Assunto: ", Input(name="assunto", type="text", required=True)),
                Label("Data: ", Input(name="data", type="date", required=True)),
                Label("Horário: ", Input(name="horario", type="time", required=True))
            ),
            Button("Criar Agenda", type="submit")
        )
    )
 
def template_buscar_agenda():
    return Titled("Buscar Agendas",
        Form(method="post", action="/buscar_agenda_por_assunto")(
            Fieldset(
                Label("Assunto: ", Input(name="assunto", type="text", required=True))
            ),
            Button("Buscar", type="submit")
        )
    )

 

def gerar_linha_agenda(agenda):
    return Tr(
        Td(agenda.assunto),
        Td(str(agenda.data)),
        Td(str(agenda.horario)),
        Td(Button("Editar", onclick=f"window.location.href='/form_editar_agenda/{agenda.id}'")),
        Td(Form(method="post", action=f"/duplicar_agenda/{agenda.id}")(
            Button("Duplicar", type="submit", style="background-color: blue; color: white;")
        )),
        Td(Form(method="post", action=f"/eliminar_agenda/{agenda.id}")(
            Button("Eliminar", type="submit", style="background-color: red; color: white;")
        ))
    )




def template_agendas_concluidas(agendas):
    if not agendas:
        return Titled("Histórico de Agendas", "Nenhuma agenda concluída foi encontrada.")

    agenda_rows = [
        Tr(
            Td(agenda["assunto"]),
            Td(agenda["data"]),
            Td(agenda["horario"])
        ) for agenda in agendas
    ]

    return Titled("Histórico de Agendas Concluídas",
        Table(
            Thead(
                Tr(
                    Th("Assunto"),
                    Th("Data"),
                    Th("Horário")
                )
            ),
            Tbody(*agenda_rows)
        )
    )

def template_relatorio_agendas(relatorio):
    # Relatório por assunto
    relatorio_assunto_rows = [
        Tr(Td(item["assunto"]), Td(item["total"])) for item in relatorio["por_assunto"]
    ]

    # Relatório por data
    relatorio_data_rows = [
        Tr(Td(item["data"]), Td(item["total"])) for item in relatorio["por_data"]
    ]

    return Titled("Relatório de Agendas",
        Titled("Por Assunto",
            Table(
                Thead(Tr(Th("Assunto"), Th("Total"))),
                Tbody(*relatorio_assunto_rows)
            )
        ),
        Titled("Por Data",
            Table(
                Thead(Tr(Th("Data"), Th("Total"))),
                Tbody(*relatorio_data_rows)
            )
        )
    )
