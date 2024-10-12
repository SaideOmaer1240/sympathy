 # Sympathy

Sympathy é uma aplicação web construída utilizando o framework **FastHTML** e **SQLAlchemy** para gerenciar consultorias online, com funcionalidades para cadastro de consultores e clientes, gerenciamento de agendas, pedidos de consultoria e avaliações. A aplicação usa JWT para autenticação e possui uma interface amigável com suporte a formulários dinâmicos e interativos.

## Funcionalidades

- **Cadastro de Consultores e Clientes:** Consultores e clientes podem se cadastrar utilizando um formulário simples.
- **Login:** Autenticação segura com suporte a tokens JWT.
- **Gerenciamento de Agendas:** Consultores podem criar, editar, duplicar e eliminar agendas, além de buscar agendas concluídas.
- **Pedidos de Consultoria:** Clientes podem buscar consultores disponíveis e realizar pedidos de consultoria.
- **Avaliação:** Clientes podem avaliar os consultores após as consultas, com notas e comentários.
- **Relatórios de Agendas:** Consultores podem gerar relatórios detalhados de suas agendas, filtrados por assunto e data.

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL-do-repositório>
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd sympathy
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Crie o arquivo `.env` e configure as variáveis de ambiente:
   ```bash
   DB_URL=postgresql://postgres:123456@localhost:5432/sympathy_db
   SECRET_KEY=sua_chave_secreta_super_segura
   ```

6. Execute as migrações do banco de dados:
   ```bash
   alembic upgrade head
   ```

7. Inicie a aplicação:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

- **/config.py**: Configuração das variáveis de ambiente.
- **/db/models.py**: Definição dos modelos de banco de dados (Consultor, Cliente, Pedido, Agenda, Avaliação).
- **/app/views.py**: Funções responsáveis pelo backend das operações de agenda, pedidos, e autenticação.
- **/app/templates**: Templates HTML gerados dinamicamente pelo FastHTML.
- **/auth/utils.py**: Funções de utilidade para geração e verificação de tokens JWT, e hash de senhas.

## Tecnologias

- **FastHTML**: Framework para desenvolvimento web em Python.
- **SQLAlchemy**: ORM para interagir com o banco de dados PostgreSQL.
- **JWT**: Utilizado para autenticação.
- **Alembic**: Gerenciador de migrações de banco de dados.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou relatar problemas na aba de *issues*.

---

Esse README cobre os principais aspectos do projeto e pode ser ajustado conforme as necessidades do seu desenvolvimento.
