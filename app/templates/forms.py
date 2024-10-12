from fasthtml.common import Titled, Fieldset, Form, Label, Input, Button, Tr, Td, Table, Thead, Tbody, Tr, Th, Td, Div, P

def template_cliente():
    return Titled("Cadastro de Cliente",
        Form(method="post", action="/cadastrar_cliente")(
            Fieldset(
                Label("Nome: ", Input(name="nome", type="text", required=True)),
                Label("Email: ", Input(name="email", type="email", required=True)),
                Label("Senha: ", Input(name="senha", type="password", required=True))
            ),
            Button("Cadastrar", type="submit")
        )
    )

def template_consultor():
    return Titled("Cadastro de Consultor",
        Form(method="post", action="/cadastrar_consultor")(
            Fieldset(
                Label("Nome: ", Input(name="nome", type="text", required=True)),
                Label("Email: ", Input(name="email", type="email", required=True)),
                Label("Área de Atuação: ", Input(name="atuacao", type="text", required=True)),
                Label("Senha: ", Input(name="senha", type="password", required=True))
            ),
            Button("Cadastrar", type="submit")
        )
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
    return Titled("Login",
        Form(method="post", action="/login")(
            Fieldset(
                Label("Email: ", Input(name="email", type="email", required=True)),
                Label("Senha: ", Input(name="senha", type="password", required=True))
            ),
            Button("Login", type="submit")
        )
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
