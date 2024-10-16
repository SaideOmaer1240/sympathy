"""criar tabelas iniciais

Revision ID: 52ce916afe2f
Revises: 
Create Date: 2024-10-10 20:47:16.311918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '52ce916afe2f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    op.drop_table('auth_group_permissions')
    op.drop_index('auth_user_groups_group_id_97559544', table_name='auth_user_groups')
    op.drop_index('auth_user_groups_user_id_6a12ed8b', table_name='auth_user_groups')
    op.drop_table('auth_user_groups')
    op.drop_index('auth_user_username_6821ab7c_like', table_name='auth_user')
    op.drop_table('auth_user')
    op.drop_index('app_thesis_author_id_d62de852', table_name='app_thesis')
    op.drop_table('app_thesis')
    op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    op.drop_table('auth_permission')
    op.drop_table('django_migrations')
    op.drop_index('accounts_userdata_author_id_499736ed', table_name='accounts_userdata')
    op.drop_table('accounts_userdata')
    op.drop_table('agenda')
    op.drop_table('django_content_type')
    op.drop_index('django_site_domain_a2e37b91_like', table_name='django_site')
    op.drop_table('django_site')
    op.drop_index('chat_message_user_id_a47c01bb', table_name='chat_message')
    op.drop_table('chat_message')
    op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c', table_name='auth_user_user_permissions')
    op.drop_index('auth_user_user_permissions_user_id_a95ead1b', table_name='auth_user_user_permissions')
    op.drop_table('auth_user_user_permissions')
    op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    op.drop_table('django_session')
    op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    op.drop_table('auth_group')
    op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    op.drop_table('django_admin_log')
    op.add_column('Agenda', sa.Column('pedido_id', sa.Integer(), nullable=False))
    op.add_column('Agenda', sa.Column('assunto', sa.String(), nullable=False))
    op.add_column('Agenda', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('Agenda', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_constraint('Agenda_consultor_id_fkey', 'Agenda', type_='foreignkey')
    op.create_foreign_key(None, 'Agenda', 'Pedido', ['pedido_id'], ['id'])
    op.drop_column('Agenda', 'consultor_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Agenda', sa.Column('consultor_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Agenda', type_='foreignkey')
    op.create_foreign_key('Agenda_consultor_id_fkey', 'Agenda', 'Consultor', ['consultor_id'], ['id'])
    op.drop_column('Agenda', 'updated_at')
    op.drop_column('Agenda', 'created_at')
    op.drop_column('Agenda', 'assunto')
    op.drop_column('Agenda', 'pedido_id')
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    )
    op.create_index('auth_user_user_permissions_user_id_a95ead1b', 'auth_user_user_permissions', ['user_id'], unique=False)
    op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', 'auth_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('chat_message',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('text', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_user', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('session_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('session_title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('image_path', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='chat_message_user_id_a47c01bb_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='chat_message_pkey')
    )
    op.create_index('chat_message_user_id_a47c01bb', 'chat_message', ['user_id'], unique=False)
    op.create_table('django_site',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('domain', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_site_pkey'),
    sa.UniqueConstraint('domain', name='django_site_domain_a2e37b91_uniq')
    )
    op.create_index('django_site_domain_a2e37b91_like', 'django_site', ['domain'], unique=False)
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('agenda',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pedido_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('assunto', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('data', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('horario', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='agenda_pkey')
    )
    op.create_table('accounts_userdata',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('professor', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('aluno', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('instituto', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('cidade', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('disciplina', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['auth_user.id'], name='accounts_userdata_author_id_499736ed_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='accounts_userdata_pkey')
    )
    op.create_index('accounts_userdata_author_id_499736ed', 'accounts_userdata', ['author_id'], unique=False)
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    op.create_table('app_thesis',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('institute', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('disciplina', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('student', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('instructor', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('cidade', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('code', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('topic', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('text', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('date_added', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('html', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['auth_user.id'], name='app_thesis_author_id_d62de852_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='app_thesis_pkey')
    )
    op.create_index('app_thesis_author_id_d62de852', 'app_thesis', ['author_id'], unique=False)
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey'),
    sa.UniqueConstraint('username', name='auth_user_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_user_username_6821ab7c_like', 'auth_user', ['username'], unique=False)
    op.create_table('auth_user_groups',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_user_groups_group_id_97559544_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
    sa.UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq')
    )
    op.create_index('auth_user_groups_user_id_6a12ed8b', 'auth_user_groups', ['user_id'], unique=False)
    op.create_index('auth_user_groups_group_id_97559544', 'auth_user_groups', ['group_id'], unique=False)
    op.create_table('auth_group_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
    sa.UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    )
    op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    # ### end Alembic commands ###
